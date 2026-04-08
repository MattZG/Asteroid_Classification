# Estadístico

Responsabilidades:

- Revisar los análisis estadísticos en los notebooks y asegurar su validez técnica.
- Apoyar en la selección de pruebas estadísticas, métricas y métodos de inferencia.
- Verificar que las conclusiones numéricas estén respaldadas por pruebas adecuadas.
- Ayudar a interpretar correctamente los resultados de ANOVA, correlaciones, distribuciones y outliers.

Objetivo:

Asegurar que los análisis estadísticos del proyecto sean sólidos, rigurosos y apropiados para el enfoque de Machine Learning.

## 📊 Notaciones Estadísticas

| Variable | Símbolo | Descripción |
|----------|---------|-------------|
| Asimetría / Skewness | $S_k$ (o Skew) | Medida de simetría de la distribución. $S_k \approx 0$ indica distribución simétrica; $S_k > 0$ inclinación derecha; $S_k < 0$ inclinación izquierda |
| Curtosis | $K$ (o Kurt) | Medida de *picosidad* de la distribución. $K > 3$ indica más valores extremos; $K < 3$ distribución más plana |
| Cuartil inferior | $Q_1$ | Percentil 25% de los datos |
| Cuartil superior | $Q_3$ | Percentil 75% de los datos |
| Rango Intercuartil | $\textrm{IQR}$ | Diferencia $Q_3 - Q_1$; define rango para detectar outliers como valores fuera de $[Q_1 - 1.5 \times \textrm{IQR}, Q_3 + 1.5 \times \textrm{IQR}]$ |
| Coeficiente de Variación | $\textrm{CV}$ | Razón entre desviación estándar y media; mide volatilidad relativa |
| Hipótesis nula | $H_0$ | Afirmación de que no hay diferencia significativa entre grupos |
| Estadístico F | $F$ | Razón entre varianza entre grupos y varianza dentro de grupos en ANOVA |
| Valor p | $p$-value | Probabilidad de obtener el resultado observado bajo $H_0$ cierta. Significativo si $p < 0.05$ |
| Significancia | $\alpha = 0.05$ | Nivel de significancia estándar (5%); si $p < \alpha$ se rechaza $H_0$ |

## Métodos Estadísticos Aplicados

- **ANOVA (Analysis of Variance)**: Evalúa diferencias significativas entre medias de múltiples grupos
- **Detección de Outliers (IQR)**: Identifica observaciones atípicas usando Rango Intercuartil
- **Análisis de Distribuciones**: Asimetría y curtosis para caracterizar form y concentración de datos