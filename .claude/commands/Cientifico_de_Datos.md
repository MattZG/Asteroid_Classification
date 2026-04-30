---
name: Cientifico_de_Datos
description: Invocar para decisiones de modelado, preprocesamiento, selección de métricas, diseño de experimentos y evaluación de resultados.
---

## Contexto del proyecto

Clasificación binaria supervisada: detectar **Objetos Potencialmente Peligrosos (PHA)** a partir de parámetros físicos y orbitales del JPL Small Body Database.

- **Dataset original**: 126.131 asteroides · 35 columnas
- **Split**: 70% trabajo (88.292 filas) · 30% validación (37.839 filas)
- **Target**: `pha` binaria (`Y` = PHA, `N` = no PHA) — fuertemente desbalanceada (~0.12%)
- **Modelo seleccionado**: XGBoost Exp B (sin `moid`), umbral = 0.078, Recall = 87.8%

## Reglas críticas de modelado

- Nunca `accuracy` como métrica — es engañosa con clases desbalanceadas. Usar F1, AUC-ROC, Precision-Recall
- Validación cruzada siempre con `StratifiedKFold` — mantiene proporción de clases en cada fold
- Sobre `validacion.csv`: solo `.transform()` — nunca `.fit()` ni `.fit_transform()`
- `validacion.csv` reservado exclusivamente para la evaluación final — no usar durante desarrollo
- Imputación con mediana, nunca con media en distribuciones asimétricas
- No incluir `spkid` ni `full_name` como features del modelo

## Dos experimentos de entrenamiento

| | Experimento A | Experimento B |
|--|---|---|
| Dataset | `trabajo_preprocesado_moid.pickle` | `trabajo_preprocesado.pickle` |
| Incluye `moid` | Sí | No |
| Problema | `moid < 0.05 UA` es parte de la definición formal de PHA → tautología | — |
| Válido para producción | No | **Sí** |

## Decisiones de preprocesamiento

**Variables eliminadas**: `moid_ld` (r=1.0 con `moid`), `ad`, `per`, `per_y`, `n` (derivadas orbitales redundantes). `spkid` y `full_name` son identificadores sin valor predictivo.

**Encoding**: `pha` → binario (Y=1/N=0). `class` → TargetEncoding (proporción suavizada de PHA por clase).

**Scaler**: `RobustScaler` — resistente a outliers. El encoding se aplica **antes** del escalado para que `class` quede como `float64`.

**Orden obligatorio del pipeline**:
1. TargetEncoder sobre `class`
2. RobustScaler sobre las 32 columnas (en el orden del scaler entrenado)
3. Drop de columnas redundantes post-escalado: `ad`, `n`, `per`, `per_y`, `moid`, `moid_ld`

## Dataset — columnas y tipos

### Identificadores (excluir del modelado)
| Columna | Descripción |
|---------|-------------|
| `spkid` | Identificador único del asteroide |
| `full_name` | Nombre completo del asteroide |

### Target
| Columna | Descripción |
|---------|-------------|
| `pha` | Binaria: `Y` (PHA) / `N` (no PHA). Clase positiva = Y. |

### Variables físicas
| Columna | Descripción |
|---------|-------------|
| `H` | Magnitud absoluta — indicador indirecto de tamaño |
| `diameter` | Diámetro estimado en km |
| `albedo` | Reflectividad superficial (0–1) |
| `diameter_sigma` | Incertidumbre del diámetro |

### Variables orbitales
| Columna | Descripción |
|---------|-------------|
| `e` | Excentricidad orbital |
| `a` | Semi-eje mayor (UA) |
| `q` | Distancia en perihelio (UA) |
| `i` | Inclinación orbital (grados) |
| `om` | Longitud del nodo ascendente |
| `w` | Argumento del perihelio |
| `ma` | Anomalía media |
| `ad` | Distancia en afelio (UA) — eliminada en preprocesamiento |
| `n` | Movimiento medio (grados/día) — eliminada en preprocesamiento |
| `tp` | Tiempo de paso por perihelio (JD) |
| `tp_cal` | Tiempo de paso por perihelio (calendario) |
| `per` | Período orbital (días) — eliminada en preprocesamiento |
| `per_y` | Período orbital (años) — eliminada en preprocesamiento |
| `moid` | Distancia mínima órbita-Tierra (UA) — variable clave para PHA |
| `moid_ld` | MOID en distancias lunares — eliminada en preprocesamiento |

### Incertidumbres orbitales
| Columna | Descripción |
|---------|-------------|
| `sigma_e` | Incertidumbre en excentricidad |
| `sigma_a` | Incertidumbre en semi-eje mayor |
| `sigma_q` | Incertidumbre en perihelio |
| `sigma_i` | Incertidumbre en inclinación |
| `sigma_om` | Incertidumbre en longitud del nodo |
| `sigma_w` | Incertidumbre en argumento del perihelio |
| `sigma_ma` | Incertidumbre en anomalía media |
| `sigma_ad` | Incertidumbre en afelio |
| `sigma_n` | Incertidumbre en movimiento medio |
| `sigma_tp` | Incertidumbre en tiempo de paso |
| `sigma_per` | Incertidumbre en período orbital |

### Calidad orbital y clasificación
| Columna | Descripción |
|---------|-------------|
| `rms` | RMS del ajuste orbital (arcsec) |
| `class` | Clase orbital del asteroide (11 categorías) |

## Decisiones de implementación por etapa

**Calidad de datos**
- `diameter` y `diameter_sigma` se cargan como `object` por valores `?` → convertir con `pd.to_numeric(..., errors='coerce')`
- Nulos resultantes: `diameter` (3), `diameter_sigma` (66) → imputar con mediana

**Entrenamiento**
- Usar `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`
- Guardar modelo siguiendo la convención de `Arquitecto_de_Codigo`
- Evaluación final sobre `validacion.csv` solo una vez al final

## Stack por etapa

| Etapa | Librerías |
|-------|-----------|
| Carga y manipulación | `pandas`, `pathlib` |
| EDA y visualización | `pandas`, `matplotlib`, `seaborn`, `scipy.stats` |
| Preprocesamiento | `scikit-learn` (`preprocessing`, `pipeline`) |
| Modelado | `scikit-learn` (`ensemble`, `tree`, `linear_model`, `model_selection`) |
| Evaluación | `scikit-learn` (`metrics`): AUC-ROC, F1, precision-recall |
| Explicabilidad | `shap` |
| Persistencia | `pickle`, `joblib` |

## Qué NO hacer

- No usar `accuracy` como métrica de evaluación
- No aplicar `.fit()` o `.fit_transform()` sobre el dataset de validación
- No evaluar sobre `validacion.csv` durante el desarrollo
- No imputar con media en distribuciones asimétricas
- No incluir `spkid` ni `full_name` como features
