# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Entorno

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

El kernel de Jupyter debe apuntar a `.\venv\Scripts\python.exe`. Si VSCode no lo detecta: Ctrl+Shift+P → "Python: Select Interpreter".

## Arquitectura del Pipeline

Proyecto de clasificación supervisada de asteroides (PHA vs. no PHA). El pipeline es una secuencia **estrictamente ordenada** de notebooks en `03_Notebooks/01_Desarrollo/`. Cada notebook consume el artefacto `.pickle` del anterior — no saltarse etapas.

```
01_Set Up          → trabajo.csv + validacion.csv
02_Calidad datos   → trabajo_resultado_calidad.pickle
03_EDA             → (solo análisis, sin artefactos)
04_Preprocesamiento→ trabajo_preprocesado_moid.pickle  (Modelo A: con moid)
                     trabajo_preprocesado.pickle        (Modelo B: sin moid)
                     04_Modelos/pipeline_scaler.joblib
                     04_Modelos/pipeline_encoder.joblib
05_Entrenamiento   → 04_Modelos/{algoritmo}_pha_{version}_pipeline.joblib
06_Resultados      → 05_Resultados/reporte_final.*
```

`02_Datos/02_Validacion/validacion.csv` no se toca hasta la evaluación final en el notebook 06.

## Patrón de Rutas (obligatorio en todos los notebooks)

```python
from pathlib import Path

repo_root = Path.cwd().resolve()
while repo_root != repo_root.parent and not (repo_root / "README.md").exists():
    repo_root = repo_root.parent

if not (repo_root / "README.md").exists():
    raise FileNotFoundError("No se encontró la raíz del repositorio (README.md).")
```

Nunca usar rutas absolutas. Construir todas las rutas a partir de `repo_root`.

## Sistema de Agentes

`01_Equipo/` contiene cinco archivos `.md` que definen roles especializados con contexto del proyecto. Se invocan mencionando el nombre del agente al inicio del mensaje. Cada agente tiene criterios propios:

| Agente | Cuándo invocarlo |
|--------|-----------------|
| `Cientifico_de_Datos` | Decisiones de modelado, preprocesamiento, métricas |
| `Astro_Fisico` | Interpretación física de variables, redundancia orbital |
| `Estadistico` | Validación de métodos estadísticos, tratamiento del desbalance |
| `Arquitecto_de_Codigo` | Rutas, estructura, convenciones de nombres, reproducibilidad |
| `Ingeniero_de_Documentacion` | Markdown en notebooks, README, mensajes de commit |

## Decisiones de Diseño Clave

**Variable target desbalanceada**: `pha = Y` representa ~2% del dataset. No usar `accuracy`. Métricas correctas: F1 (clase PHA), AUC-ROC, Precision-Recall. Validación cruzada siempre con `StratifiedKFold`.

**Dos experimentos de entrenamiento**:
- Modelo A (`trabajo_preprocesado_moid.pickle`): incluye `moid`. `moid < 0.05 UA` es parte de la definición formal de PHA, lo que puede inflar métricas.
- Modelo B (`trabajo_preprocesado.pickle`): excluye `moid`. Variables físicas puras.

**Variables eliminadas en preprocesamiento**: `moid_ld` (r=1.0 con `moid`), `ad`, `per`, `per_y`, `n` (derivadas orbitales redundantes). `spkid` y `full_name` son identificadores sin valor predictivo.

**Encoding**: `pha` → binario (Y=1/N=0). `class` → TargetEncoding (proporción suavizada de PHA por clase). Scaler: `RobustScaler` (resistente a outliers). El encoding se aplica **antes** del escalado para que `class` quede como `float64`.

## Convenciones de Commits

Frases cortas en pasado, en español, sin puntuación final, sin Co-Authored-By:

```
Se completó la etapa de Preprocesamiento
Se actualizaron los agentes del equipo
Se agregó análisis de importancia de variables
```

## Nombres de Artefactos en `04_Modelos/`

```
{algoritmo}_pha_{version}_pipeline.joblib   # pipeline completo para predicción
{algoritmo}_pha_{version}_metricas.json     # métricas de esa versión
```

Abreviaturas: `logreg`, `rfc`, `dtc`, `xgb`, `lgbm`, `svc`, `knn`.

## Qué NO Hacer

- No imputar con la media en distribuciones asimétricas — usar mediana
- No usar `accuracy` como métrica en clasificación desbalanceada
- No incluir `spkid` ni `full_name` como features del modelo
- No aplicar transformaciones del dataset de trabajo al dataset de validación por separado — usar los mismos transformadores entrenados en trabajo (`.fit_transform()` en trabajo, `.transform()` en validación)
- No evaluar sobre validación durante el desarrollo — reservar exclusivamente para la evaluación final

## Estado actual

- [x] Setup
- [x] Calidad de datos
- [x] EDA
- [x] Preprocesamiento
- [ ] Entrenamiento
- [ ] Analisis del modelo
- [ ] Produccion