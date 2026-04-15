# Proyecto: Clasificación de Asteroides

## Objetivo

Desarrollar un pipeline de Machine Learning para clasificar asteroides usando características físicas y orbitales, con énfasis en la detección de Objetos Potencialmente Peligrosos (PHA) y en la interpretación astrofísica de los resultados.

El proyecto combina calidad de datos, análisis exploratorio y modelado supervisado para generar una solución reproducible y científicamente rigurosa.

## Dataset

- **Fuente**: JPL Small Body Database
- **Tamaño**: 126.131 asteroides · 35 variables
- **Variable target**: `pha` (binaria: Y = potencialmente peligroso / N = no peligroso)
- **Split**: 70% entrenamiento (88.292 filas) · 30% validación (37.839 filas)

## Estructura del Proyecto

```
Asteroid_Classification/
├── 01_Equipo/               ← agentes especializados del proyecto
├── 02_Datos/
│   ├── 01_Originales/       ← dataset original (inmutable)
│   ├── 02_Validacion/       ← dataset de validación (reservado para evaluación final)
│   ├── 03_Trabajo/          ← artefactos intermedios del pipeline
│   └── 04_Caches/
├── 03_Notebooks/
│   ├── 01_Desarrollo/       ← pipeline de desarrollo (6 etapas)
│   └── 03_Sistema/          ← notebooks de producción
├── 04_Modelos/              ← modelos y pipelines serializados
├── 05_Resultados/           ← métricas y reportes de evaluación final
└── requirements.txt
```

## Pipeline de Desarrollo

| # | Notebook | Descripción |
|---|----------|-------------|
| 01 | Set Up | Carga del dataset original, división trabajo/validación |
| 02 | Calidad de datos | Revisión de tipos, nulos, duplicados y correcciones |
| 03 | EDA | Análisis exploratorio: distribuciones, ANOVA, correlaciones, visualizaciones |
| 04 | Preprocesamiento | Homogeneización, codificación, escalado y tratamiento del desbalance |
| 05 | Entrenamiento ML | Entrenamiento, validación cruzada y selección del modelo |
| 06 | Análisis de Resultados | Evaluación final sobre validación, importancia de variables y conclusiones |

## Estado del Proyecto

| Etapa | Estado |
|-------|--------|
| Set Up | Completado |
| Calidad de datos | Completado |
| EDA | Completado |
| Preprocesamiento | En curso |
| Entrenamiento ML | Pendiente |
| Análisis de Resultados | Pendiente |
| Producción | Pendiente |
