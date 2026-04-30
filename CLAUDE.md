# CLAUDE.md

## Proyecto

Clasificación supervisada de asteroides para detectar **Objetos Potencialmente Peligrosos (PHA)** usando el JPL Small Body Database (126.131 asteroides, 35 variables físicas y orbitales).

El objetivo es construir un pipeline de ML reproducible que, dado un conjunto de parámetros orbitales de un asteroide nuevo, prediga si representa un riesgo potencial para la Tierra — sin depender de `moid`, que forma parte de la definición formal de PHA y produce tautología.

**Modelo seleccionado**: XGBoost — Experimento B (sin `moid`), umbral F2-óptimo = 0.078, Recall = 87.8% sobre validación independiente.

## Estado del pipeline

- [x] Setup
- [x] Calidad de datos
- [x] EDA
- [x] Preprocesamiento
- [x] Entrenamiento
- [x] Análisis de resultados
- [ ] Producción

## Skills del proyecto

Skills especializados con contexto detallado del proyecto. Se invocan con `/NombreSkill`:

`/Cientifico_de_Datos` · `/Astro_Fisico` · `/Estadistico` · `/Arquitecto_de_Codigo` · `/Ingeniero_de_Documentacion`

## Idioma

Responder en español neutro, sin regionalismos ni modismos.