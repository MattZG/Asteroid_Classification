# Astro Físico

Responsabilidades:

- Evaluar la relevancia científica del proyecto en el contexto de asteroides.
- Revisar las variables del dataset para asegurar que tengan sentido físico.
- Aportar perspectiva sobre los datos astronómicos y su interpretación.
- Sugerir mejoras basadas en conocimientos de astrofísica y objetivos de clasificación.

Objetivo:

Asegurar que el proyecto mantenga coherencia científica y valor astronómico.

## 🌌 Notaciones Astrofísicas

| Parámetro | Símbolo | Significado Físico |
|-----------|---------|-------------------|
| Magnitud Absoluta | $H$ | Brillo intrínseco del asteroide; indicador indirecto de tamaño/reflectividad. Valores menores = objetos más brillantes |
| Diámetro | $D$ | Tamaño físico estimado del asteroide en km |
| Albedo | $A$ | Reflectividad superficial (0 ≤ $A$ ≤ 1). Bajo: carbonoso oscuro; Alto: rocoso/metálico |
| Excentricidad | $e$ | Describe forma orbital (0 ≤ $e$ < 1). $e \approx 0$: órbita casi circular; $e$ alto: órbita elíptica alargada |
| Semi-eje mayor | $a$ | Tamaño de la órbita (en UA); define posición orbital y período de revolución |
| Perihelio | $q$ | Distancia más cercana al Sol; $q = a(1-e)$ |
| Afelio | $Q$ | Distancia más lejana del Sol; $Q = a(1+e)$ |
| Inclinación | $i$ | Ángulo de la órbita respecto plano de referencia (0° = en el plano; >30° = poblaciones diferentes) |
| Longitud nodo ascendente | $\Omega$ (om) | Ángulo de orientación orbital en el plano de referencia |
| Argumento del perihelio | $\omega$ (w) | Orientación de la órbita (posición del perihelio en órbita) |
| Anomalía media | $M$ (ma) | Parámetro de posición angular del asteroide en su órbita en referencia temporal |
| Distancia mínima Tierra-órbita | $\textrm{MOID}$ | Distancia mínima entre órbita del asteroide y de la Tierra (UA). **PHA si MOID < 0.05 UA** |
| Incertidumbre en parámetro $X$ | $\sigma_X$ | Error/precisión de medición de parámetro $X$; usado para filtrar datos de baja calidad |
| Ajuste orbital RMS | $\textrm{RMS}$ | Precisión del ajuste del modelo orbital a las observaciones |

## Conceptos Astrofísicos Clave

- **Clasificación PHA**: Objetos Potencialmente Peligrosos con distancia mínima $\textrm{MOID} < 0.05$ UA a la órbita terrestre
- **Parámetros Orbitales Osculating**: Definen la órbita del asteroide en un instante dado de referencia
- **Separabilidad por Discriminantes**: Variables $\textrm{MOID}$, $a$, $e$, $H$, $D$ son altamente discriminantes entre clases