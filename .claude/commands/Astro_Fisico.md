---
name: Astro_Fisico
description: Invocar para interpretacion fisica de variables orbitales, validacion de criterios de calidad de observacion, clasificacion de tipos de asteroides y coherencia fisica de los resultados del modelo.
---

## Contexto del proyecto

Pipeline de ML para detectar Objetos Potencialmente Peligrosos (PHA). Dataset: 126.131 asteroides con parametros fisicos, orbitales y metricas de calidad, JPL Small Body Database.

Distincion clave: no todas las columnas son variables del problema. Un subconjunto son metricas de incertidumbre orbital. Confundirlos tiene consecuencias fisicas directas.

---

## Variables del Problema vs. Incertidumbre Orbital

### Variables del Problema

| Columna | Rol fisico |
|---------|------------|
| H | Magnitud absoluta - proxy de tamano y reflectividad |
| diameter | Diametro estimado en km |
| albedo | Reflectividad superficial (0-1) |
| diameter_sigma | Incertidumbre del diametro |
| e | Excentricidad orbital |
| a | Semi-eje mayor (UA) |
| q | Distancia en perihelio: q = a(1-e) |
| i | Inclinacion orbital (grados) |
| om | Longitud del nodo ascendente |
| w | Argumento del perihelio |
| ma | Anomalia media |
| ad | Distancia en afelio: Q = a(1+e) |
| n | Movimiento medio (grados/dia) |
| tp | Tiempo de paso por perihelio (JD) |
| tp_cal | Tiempo de paso por perihelio (calendario) |
| per | Periodo orbital (dias) |
| per_y | Periodo orbital (anos) |
| moid | Distancia minima orbita asteroide-Tierra (UA) - variable mas discriminante para PHA |
| moid_ld | MOID en distancias lunares |
| rms | RMS del ajuste orbital en arcsec |
| class | Clase dinamica del asteroide |

### Variables de Incertidumbre Orbital (sigma_*)

No describen el asteroide: describen la precision con la que conocemos su orbita.

| Columna | Parametro |
|---------|-----------|
| sigma_e | Incertidumbre en excentricidad |
| sigma_a | Incertidumbre en semi-eje mayor |
| sigma_q | Incertidumbre en distancia de perihelio |
| sigma_i | Incertidumbre en inclinacion |
| sigma_om | Incertidumbre en longitud del nodo ascendente |
| sigma_w | Incertidumbre en argumento del perihelio |
| sigma_ma | Incertidumbre en anomalia media |
| sigma_ad | Incertidumbre en distancia de afelio |
| sigma_n | Incertidumbre en movimiento medio |
| sigma_tp | Incertidumbre en tiempo de paso por perihelio |
| sigma_per | Incertidumbre en periodo orbital |

Las incertidumbres varian varios ordenes de magnitud entre asteroides bien observados y objetos recien descubiertos. Es comportamiento fisico esperado. Su uso principal es como filtro de calidad, no como features del modelo.

---

## Criterios de Observacion No Confiable

### Criterio 1 - Incertidumbre Relativa

sigma_X / |X| > 0.10 implica parametro X con calidad insuficiente.

| Parametro | Criterio | Consecuencia fisica |
|-----------|----------|---------------------|
| sigma_a / a > 0.10 | Semi-eje mayor impreciso | La clase orbital puede ser erronea |
| sigma_e / e > 0.10 | Excentricidad imprecisa | q y Q derivados no son confiables |
| sigma_q / q > 0.20 | Perihelio impreciso | Determinacion PHA por MOID ~0.05 UA es ambigua |
| sigma_i / i > 0.10 | Inclinacion imprecisa | Separacion entre poblaciones orbitales incierta |

### Criterio 2 - Calidad del Ajuste Orbital (RMS)

| Valor RMS | Calidad | Recomendacion |
|-----------|---------|---------------|
| rms < 0.5 | Excelente | Usar con plena confianza |
| 0.5 <= rms < 1.0 | Aceptable | Usar con precaucion para PHAs frontera |
| rms >= 1.0 | Deficiente | Marcar como no confiable |

### Criterio 3 - Ambiguedad de Clasificacion PHA

Asteroide en zona frontera (MOID entre 0.03 y 0.07 UA) es ambiguo si MOID +/- 3*sigma_q cruza el umbral de 0.05 UA.

---

## Tipos de Asteroides en el Dataset

| Clase | Nombre | Rango orbital | Caracteristicas |
|-------|--------|---------------|-----------------|
| IEO | Interior Earth Objects | Q < 0.983 UA | Orbita completamente interior a la Tierra. Muy raros. |
| ATE | Atens | a < 1.0 UA, Q > 0.983 UA | NEA con semi-eje menor que la Tierra. |
| APO | Apollos | a >= 1.0 UA, q < 1.017 UA | NEA que cruzan la orbita terrestre. Mayor proporcion de PHA. |
| AMO | Amors | 1.017 < q < 1.3 UA | NEA que se aproximan pero no cruzan la orbita terrestre. |
| MCA | Mars-Crossers | q < 1.666 UA, no NEA | Cruzan la orbita de Marte. |
| IMB | Inner Main Belt | a < 2.5 UA | Cinturon interior. |
| MBA | Main Belt Asteroids | 2.5 <= a <= 3.2 UA | Clase mas numerosa del dataset. |
| OMB | Outer Main Belt | 3.2 < a <= 4.6 UA | Cinturon exterior. |
| TJN | Jupiter Trojans | 4.6 < a <= 5.5 UA | Puntos de Lagrange L4 y L5 de Jupiter. |
| CEN | Centaurs | 5.5 < a <= 30.1 UA | Entre Jupiter y Neptuno. Orbitas inestables. |
| TNO | Trans-Neptunians | a > 30.1 UA | Mas alla de Neptuno. |

PHA posibles: solo IEO, ATE, APO y AMO. MBA, OMB, TJN, CEN, TNO no pueden ser PHA por definicion orbital.

---

## Conceptos Astrofisicos Clave

- Clasificacion PHA: MOID < 0.05 UA y H < 22.
- Parametros Osculadores: los parametros orbitales describen la orbita en un instante de referencia (epoca).
- Variables mas discriminantes para PHA: moid, q, a, e, H.
- Redundancia orbital: q, ad, per, per_y, n son derivadas de a y e. Incluir ambas introduce multicolinealidad.
- q es condicion necesaria pero no suficiente para PHA: MOID depende tambien de omega, Omega, i. Un asteroide puede tener q bajo y MOID alto si sus planos orbitales estan muy inclinados respecto al de la Tierra. Este es el limite fisico del modelo sin moid.
- Incertidumbres como proxy de cobertura observacional: valores bajos de sigma_* indican asteroides con muchas observaciones. Valores altos indican descubrimientos recientes.
