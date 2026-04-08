from pathlib import Path
import json

path = Path('03_Notebooks/01_Desarrollo/03_EDA.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))

# Update celda 31 (Interpretación Física) with full LaTeX and graphics
interpretation_updated = [
    '## 2. Interpretación Física :robot:\n',
    '\n',
    'En esta sección el Astro Físico interpreta qué significa cada variable del dataset y cómo se relaciona con el comportamiento orbital y físico de los asteroides, utilizando notación LaTeX para precisión.\n',
    '\n',
    '### Significado de las principales variables\n',
    '\n',
    '**Características Físicas:**\n',
    '- **$H$ (Magnitud Absoluta)**: indicador indirecto del tamaño y la reflectividad. Valores más bajos corresponden a objetos más brillantes o grandes. Ver histogramas en 4.1.\n',
    '- **$D$ (Diámetro)**: estimación del tamaño físico del asteroide. Los histogramas muestran una distribución con sesgo derecho (skew > 0), indicando presencia de asteroides muy grandes pero poco frecuentes.\n',
    '- **$A$ (Albedo)**: reflectividad de la superficie ($0 \\leq A \\leq 1$). Indica tipo de material: asteroides oscuros ($A$ bajo) suelen ser carbonosos; $A$ alto indica composición rocosa o metálica. Los boxplots por clase (4.5) muestran diferencias significativas.\n',
    '\n',
    '**Parámetros Orbitales:**\n',
    '- **$e$ (Excentricidad)**: describe cuán elongada es la órbita ($0 \\leq e < 1$ para órbitas elípticas). Valores cercanos a cero indican órbitas casi circulares; valores altos indican órbitas muy elípticas. La relación entre $e$ y $a$ se visualiza en 4.4.\n',
    '- **$a$ (Semi-eje Mayor)**: controla el tamaño de la órbita. Asteroides de distintas clases suelen agruparse en rangos distintos de $a$, como se ve en los boxplots (4.5) y violines (4.6).\n',
    '- **$q$ (Perihelio) y $Q$ (Afelio)**: $q = a(1-e)$ y $Q = a(1+e)$ describen la distancia al Sol en los puntos más cercano y lejano. Juntas con $a$ y $e$, determinan el rango orbital.\n',
    '- **$i$ (Inclinación)**: inclinación de la órbita respecto al plano orbital de referencia. Valores cercanos a 0° indican órbitas en el plano; valores mayores a 30° o más indican poblaciones diferentes. Ver scatterplots (4.4).\n',
    '- **$\\Omega$ (om) y $\\omega$ (w)**: describen la orientación de la órbita en el espacio. En este dataset, $\\Omega$ muestra significancia estadística (ANOVA $p < 0.05$), pero $\\omega$ no. Estos parámetros definen la geometría pero no el tamaño de la órbita.\n',
    '- **$M$ (Anomalía Media)**: parámetro de posición a lo largo de la órbita en el momento de referencia. Valores uniformes (0–360°) indican que no hay preferencia temporal.\n',
    '- **$\\textrm{MOID}$**: distancia mínima entre la órbita del asteroide y la de la Tierra. Es fundamental para clasificar PHA: MOID < 0.05 UA es criterio para PHA. Los gráficos orbitales en 4.10 muestran cómo varían las órbitas por clase.\n',
    '- **Variables $\\sigma_X$**: representan incertidumbres en cada parámetro. Son relevantes para filtrar o ponderar observaciones de baja calidad en el modelado.\n',
    '\n',
    '### Interpretación astrofísica general\n',
    '\n',
    'Los resultados ANOVA (sección 1, Test ANOVA) muestran que casi todas las variables tienen diferencias significativas entre clases, lo que es consistente con la existencia de poblaciones de asteroides orbital y físicamente distintas.\n',
    '\n',
    'En particular:\n',
    '- Parámetros como $\\textrm{MOID}$, $a$, $e$, $D$ y $H$ son discriminantes clave, reflejando diferencias en riesgo de aproximación y composición.\n',
    '- Variables de orientación ($\\omega$) son menos discriminantes estadísticamente, indicando que la geometría de la órbita por sí sola no separa bien las clases.\n',
    '- Las magnitudes de los estadísticos F (tabla ANOVA) sugieren que $a$, $e$, y parámetros relacionados con el riesgo ($\\textrm{MOID}$) son las más separadoras.\n',
    '- Los gráficos orbitales (4.10.1 y 4.10.2) permiten visualizar estas diferencias en el espacio 2D y 3D, confirmando que las órbitas de distintas clases ocupan regiones distintas.\n',
    '\n',
    'Esta separación clara motiva el uso de técnicas supervisadas para clasificar asteroides basándose en sus propiedades astrofísicas.\n'
]
nb['cells'][31]['source'] = interpretation_updated

# Update the Outliers reference in Análisis Estadístico
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown' and '### 3.3 Outliers' in ''.join(cell['source']):
        # Next cell should have the explanation; update it
        if i+1 < len(nb['cells']):
            nb['cells'][i+1]['source'] = [
                'Se utiliza el método del rango intercuartil (IQR) para detectar outliers: valores fuera del rango $[Q_1 - 1.5 \\times \\textrm{IQR}, Q_3 + 1.5 \\times \\textrm{IQR}]$ se consideran atípicos.\n',
                '\n',
                'Los boxplots en la sección 4.2 visualizan estos valores extremos; es importante notar que para variables con altos niveles de outliers, modelos robustos serán preferibles.\n'
            ]
        break

path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
