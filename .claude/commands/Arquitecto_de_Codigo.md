---
name: Arquitecto_de_Codigo
description: Invocar para decisiones sobre estructura de carpetas, patrones de rutas, convenciones de nombres, organización de notebooks y reproducibilidad del pipeline.
---

## Estructura del proyecto

```
Asteroid_Classification/           ← raíz del repositorio (contiene README.md)
│
├── .claude/commands/              ← Skills especializados del proyecto (slash commands)
├── 01_Datos/
│   ├── 01_Originales/             ← Asteroid_Dataset.csv — inmutable, nunca modificar
│   ├── 02_Validacion/             ← validacion.csv — no tocar hasta evaluación final
│   └── 03_Trabajo/                ← artefactos intermedios del pipeline (.pickle, .csv)
├── 02_Notebooks/
│   ├── 01_Desarrollo/             ← pipeline principal (01 al 06, orden estricto)
│   └── 02_Produccion/             ← notebooks de producción e inferencia
├── 03_Modelos/                    ← artefactos serializados: transformadores y modelos
├── 04_Resultados/01_Analisis/                 ← gráficos, métricas y reportes de evaluación
├── README.md                      ← ancla de la raíz del repositorio
└── requirements.txt
```

## Pipeline — flujo de artefactos

Secuencia estrictamente ordenada. Cada notebook consume el artefacto del anterior.

```
01_Set_Up           → 01_Datos/03_Trabajo/trabajo.csv
                      01_Datos/02_Validacion/validacion.csv
02_Calidad_de_datos → 01_Datos/03_Trabajo/trabajo_resultado_calidad.pickle
03_EDA              → (solo análisis, sin artefactos)
04_Preprocesamiento → 01_Datos/03_Trabajo/trabajo_preprocesado_moid.pickle  (Exp A)
                      01_Datos/03_Trabajo/trabajo_preprocesado.pickle        (Exp B)
                      03_Modelos/pipeline_scaler.joblib
                      03_Modelos/pipeline_encoder.joblib
05_Entrenamiento    → 03_Modelos/{algoritmo}_pha_{experimento}_{version}_pipeline.joblib
06_Analisis         → 04_Resultados/01_Analisis/*.png  +  04_Resultados/01_Analisis/seleccion_modelo_final.json
02_Produccion/
  01_Preproduccion  → 04_Resultados/01_Analisis/02_Preproduccion/metricas_validacion.json
  02_Produccion     → 04_Resultados/01_Analisis/03_Produccion/reporte_produccion.csv  +  reporte_produccion.json
```

## Patrón de rutas (obligatorio en todos los notebooks)

```python
from pathlib import Path

repo_root = Path.cwd().resolve()
while repo_root != repo_root.parent and not (repo_root / "README.md").exists():
    repo_root = repo_root.parent

if not (repo_root / "README.md").exists():
    raise FileNotFoundError("No se encontró la raíz del repositorio (README.md).")
```

Nunca rutas absolutas. Todas las rutas parten de `repo_root`. Nunca usar `os.chdir()`.

## Convenciones de nombres

**Archivos y carpetas**: guion bajo `_` en lugar de espacios. Ejemplos: `01_Set_Up.ipynb`, `02_Calidad_de_datos.ipynb`.

**Artefactos en `03_Modelos/`**:
```
{algoritmo}_pha_{experimento}_{version}_pipeline.joblib   # pipeline completo
{algoritmo}_pha_{experimento}_{version}_metricas.json     # métricas de esa versión
```
- Experimentos: `A` (con `moid`), `B` (sin `moid`)
- Algoritmos: `logreg`, `rfc`, `dtc`, `xgb`, `lgbm`, `svc`, `knn`
- Versiones: `v1`, `v2` — nunca fechas en el nombre

## Convenciones de notebooks

- Todos los `import` van en la celda de Sección 1 — nunca inline en la celda donde se usa
- Numeración secuencial dentro de cada carpeta: `01_`, `02_`, etc.
- `03_Modelos/` solo contiene artefactos serializados — no scripts ni notebooks

## Reglas de estructura

- `01_Datos/01_Originales/` es inmutable — nunca se sobreescribe el dataset original
- `01_Datos/02_Validacion/` no se modifica después del Set Up
- `03_Modelos/` contiene los transformadores ajustados en preprocesamiento (`pipeline_scaler.joblib`, `pipeline_encoder.joblib`) y los modelos entrenados
- No duplicar artefactos entre carpetas — cada carpeta tiene un rol exclusivo

## Qué NO hacer

- No usar rutas absolutas — rompen al cambiar de máquina
- No usar `os.chdir()` dentro de notebooks
- No nombrar artefactos con fechas (`modelo_20240315.pkl`) — usar versiones (`v1`, `v2`)
- No dejar notebooks sin número de orden o con nombres inconsistentes
- No poner imports inline fuera de la Sección 1
