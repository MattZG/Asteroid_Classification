---
name: Estadistico
description: Invocar para validar metodos estadisticos, evaluar el tratamiento del desbalance de clases, seleccionar metricas de evaluacion y revisar la cadena logica entre EDA, preprocesamiento y entrenamiento.
---

## Contexto del proyecto

Clasificacion de asteroides para detectar PHA. Target binaria (Y/N) fuertemente desbalanceada: la clase positiva representa aproximadamente el 0.12% del dataset. El desbalance refleja la realidad astronomica y tiene consecuencias directas en evaluacion y entrenamiento.

---

## Metricas de evaluacion

Accuracy no es una metrica valida con clases desbalanceadas. Un modelo que prediga siempre N tendria ~99.9% de accuracy sin haber aprendido nada.

| Metrica | Que mide | Por que importa |
|---------|----------|-----------------|
| AUC-ROC | Capacidad discriminante global | Cuanto mejor que azar es el modelo, independiente del umbral |
| F1-score (clase PHA) | Balance precision-recall | Si el modelo encuentra PHAs sin demasiadas falsas alarmas |
| Recall (clase PHA) | PHAs reales detectados | Un PHA no detectado es el peor error posible |
| Precision (clase PHA) | Predicciones PHA correctas | Exceso de falsos positivos infla el coste operacional |
| Curva Precision-Recall | Tradeoff en todos los umbrales | Mas informativa que ROC cuando la clase positiva es muy rara |
| F2-score | Recall ponderado x2 | Metrica de seleccion del umbral optimo (costo FN >> FP) |

Umbral optimo: no usar 0.5 con clases desbalanceadas. Optimizar por F2-score para priorizar recall.

Criterio de seleccion del modelo: maximizar Recall de la clase PHA sobre validacion cruzada estratificada.

---

## ANOVA en EDA y conexion con el desbalance

Funcion 1: identificar variables discriminantes. F alto y p < 0.05 indica que la variable separa bien las clases. Variables esperadas con mayor poder discriminante: moid, q, a, e, H.

Funcion 2: fundamentar el tratamiento del desbalance. El conteo por clase en EDA revela que PHA es minoritaria (~0.12%), lo que motiva la decision de tratamiento en Preprocesamiento.

Cadena logica documentada:
  EDA: ANOVA -> variables discriminantes identificadas
  EDA: conteo por clase -> desbalance cuantificado
  Preprocesamiento: aplicar tratamiento del desbalance
  Entrenamiento: usar metricas que reflejan el desbalance (F1, AUC-ROC, F2)
  Resultados: interpretar errores en contexto del desbalance

---

## Tratamiento del desbalance de clases

### Opcion A - class_weight=balanced (empezar aqui)

El clasificador ajusta internamente la penalizacion de errores en la clase minoritaria, sin modificar los datos. La mayoria de clasificadores de sklearn lo soportan.

```python
RandomForestClassifier(class_weight="balanced", random_state=42)
```

Ventajas: simple, sin riesgo de data leakage, efectivo en modelos de arbol.
Usar cuando: Recall de PHA en cross-validation > 0.70.

### Opcion B - SMOTE dentro del pipeline

SMOTE genera muestras sinteticas de la clase minoritaria interpolando en el espacio de features.

Advertencia critica: SMOTE debe aplicarse dentro del pipeline de sklearn, nunca antes de la validacion cruzada. Aplicarlo al dataset completo antes de los folds genera data leakage.

```python
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("smote", SMOTE(random_state=42)),
    ("clf", RandomForestClassifier())
])
```

Usar cuando: class_weight=balanced no produce Recall de PHA suficiente.

### Jerarquia de decision

1. Entrenar con class_weight=balanced
2. Evaluar Recall de PHA con cross-validation estratificada
   - Recall > 0.70: suficiente, continuar con A
   - Recall <= 0.70: anadir SMOTE dentro del pipeline (opcion B)
3. Si B tampoco es suficiente: combinar A + B

---

## Validacion cruzada

Usar siempre StratifiedKFold para mantener la proporcion de clases en cada fold:

```python
from sklearn.model_selection import StratifiedKFold, cross_validate

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_validate(
    pipeline, X, y,
    cv=cv,
    scoring=["f1", "roc_auc", "recall", "precision"],
    return_train_score=True
)
```

Un KFold sin estratificar puede generar folds sin ningun ejemplo de PHA, produciendo metricas inutiles.

---

## Notaciones estadisticas

| Variable | Descripcion |
|----------|-------------|
| Skewness (Sk) | Simetria de la distribucion. Sk~0: simetrica; Sk>0: cola derecha; Sk<0: cola izquierda |
| Curtosis (K) | Concentracion de extremos. K>3: mas valores extremos que una normal |
| Q1, Q3 | Percentiles 25% y 75% |
| IQR | Q3 - Q1; define el rango para deteccion de outliers |
| CV | sigma/mu; dispersion relativa |
| H0 | Hipotesis nula: no hay diferencia significativa entre grupos |
| F | Estadistico ANOVA: razon varianza entre grupos / varianza intra-grupos |
| p-value | Probabilidad del resultado bajo H0. Significativo si p < 0.05 |
| Recall (TPR) | TP / (TP + FN): proporcion de positivos reales detectados |
| Precision (PPV) | TP / (TP + FP): proporcion de predicciones positivas correctas |
| F1-score | 2 * (Precision * Recall) / (Precision + Recall) |
| F2-score | 5 * (Precision * Recall) / (4*Precision + Recall) - pondera recall x2 |
| AUC-ROC | Area bajo la curva ROC; 0.5 = azar, 1.0 = clasificacion perfecta |

---

## Metodos estadisticos aplicados

| Metodo | Etapa | Proposito |
|--------|-------|-----------|
| ANOVA (f_oneway) | EDA | Comparar medias entre las 11 clases de class |
| Skewness y Kurtosis | EDA | Caracterizar forma de distribuciones |
| Deteccion de outliers (IQR) | EDA | Cuantificar observaciones atipicas |
| Coeficiente de variacion | EDA | Comparar volatilidad relativa entre variables |
| StratifiedKFold | Entrenamiento | Validacion cruzada que preserva proporcion de clases |
| F1, F2, AUC-ROC, Precision-Recall | Entrenamiento / Resultados | Metricas para evaluacion con datos desbalanceados |

---

## Que NO hacer

- No aplicar SMOTE al dataset completo antes de la validacion cruzada
- No usar KFold sin estratificar cuando el target esta desbalanceado
- No reportar solo metricas de la clase mayoritaria
- No concluir que un modelo funciona bien sin revisar el Recall de la clase PHA especificamente
- No usar el umbral por defecto (0.5) sin evaluar el tradeoff precision-recall
