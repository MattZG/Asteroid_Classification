import json
from pathlib import Path

# Cargar notebook
nb_path = Path('03_Notebooks/01_Desarrollo/03_EDA.ipynb')
with open(nb_path, encoding='utf-8') as f:
    nb = json.load(f)

# Definir variables y sus símbolos
# Primero aparecen como "variable nombre $símbolo$"
# Después solo "$símbolo$"

# Patrón: (nombre_palabra_clave, símbolo_latex, descripción_corta)
variables_first_mention = {
    'H': ('magnitud absoluta $H$', 'brillo', 'indicador indirecto del tamaño y reflectividad'),
    'diameter': ('diámetro $D$', 'tamaño', 'estimación del tamaño físico'),
    'albedo': ('albedo $A$', 'reflectividad', 'reflectividad de la superficie'),
    'e': ('excentricidad $e$', 'elongación', 'describe cuán elongada es la órbita'),
    'a': ('semi-eje mayor $a$', 'tamaño orbital', 'controla el tamaño de la órbita'),
    'q': ('perihelio $q$', 'distancia cercana', 'distancia mínima al Sol'),
    'ad': ('afelio $Q$', 'distancia lejana', 'distancia máxima al Sol'),
    'i': ('inclinación $i$', 'ángulo orbital', 'inclinación de la órbita'),
    'om': ('longitud nodo ascendente $\\Omega$', 'om', 'orientación del nodo'),
    'w': ('argumento del perihelio $\\omega$', 'w', 'orientación del perihelio'),
    'ma': ('anomalía media $M$', 'posición angular', 'parámetro de posición orbital'),
    'moid': ('distancia mínima a Tierra $\\textrm{MOID}$', 'criterio PHA', 'fundamental para clasificar PHA'),
}

# Buscar la sección 2 "Interpretación Física" 
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        content = ''.join(cell['source'])
        if 'Interpretación Física' in content and 'astrofísica general' in content:
            # Esta es la celda que debe refactorizarse
            print(f"Encontrada celda Interpretación Física en posición {i}")
            print("Contenido actual (primeras 500 chars):")
            print(content[:500])
            print("\nProcediendo a refactorizar...\n")
            
            # Nueva versión refactorizada con patrón correcto
            new_content = """## 2. Interpretación Física :robot:

En esta sección el Astro Físico interpreta qué significa cada variable del dataset y cómo se relaciona con el comportamiento orbital y físico de los asteroides, utilizando notación LaTeX para precisión.

### Significado de las principales variables

**Características Físicas:**
- **Magnitud absoluta $H$**: indicador indirecto del tamaño y la reflectividad. Valores más bajos corresponden a objetos más brillantes o grandes. Ver histogramas en 4.1.
- **Diámetro $D$**: estimación del tamaño físico del asteroide. Los histogramas muestran una distribución con sesgo derecho (skew > 0), indicando presencia de asteroides muy grandes pero poco frecuentes.
- **Albedo $A$**: reflectividad de la superficie ($0 \leq A \leq 1$). Indica tipo de material: asteroides oscuros ($A$ bajo) suelen ser carbonosos; $A$ alto indica composición rocosa o metálica. Los boxplots por clase (4.5) muestran diferencias significativas entre $A$ en distintas clases.

**Parámetros Orbitales:**
- **Excentricidad $e$**: describe cuán elongada es la órbita ($0 \leq e < 1$ para órbitas elípticas). Valores cercanos a cero indican órbitas casi circulares; valores altos indican órbitas muy elípticas. La relación entre $e$ y $a$ se visualiza en 4.4.
- **Semi-eje mayor $a$**: controla el tamaño de la órbita. Asteroides de distintas clases suelen agruparse en rangos distintos de $a$, como se ve en los boxplots (4.5) y violines (4.6).
- **Perihelio $q$ y Afelio $Q$**: $q = a(1-e)$ y $Q = a(1+e)$ describen la distancia al Sol en los puntos más cercano y lejano. Junto con $a$ y $e$, determinan el rango orbital completo.
- **Inclinación $i$**: inclinación de la órbita respecto al plano orbital de referencia. Valores cercanos a 0° indican órbitas en el plano; valores mayores a 30° indican poblaciones diferentes. Ver scatterplots (4.4).
- **Longitud nodo ascendente $\Omega$ y Argumento del perihelio $\omega$**: describen la orientación de la órbita en el espacio. En este dataset, $\Omega$ muestra significancia estadística (ANOVA $p < 0,05$), pero $\omega$ no. Estos parámetros definen la geometría pero no el tamaño de la órbita.
- **Anomalía media $M$**: parámetro de posición a lo largo de la órbita en el momento de referencia. Valores uniformes (0–360°) indican que no hay preferencia temporal.
- **Distancia mínima a Tierra $\textrm{MOID}$**: distancia mínima entre la órbita del asteroide y la de la Tierra. Es fundamental para clasificar PHA: $\textrm{MOID} < 0,05$ UA es criterio para PHA. Los gráficos orbitales en 4.10 muestran cómo varían las órbitas por clase.
- **Variables $\sigma_X$**: representan incertidumbres en cada parámetro. Son relevantes para filtrar o ponderar observaciones de baja calidad en el modelado.

### Interpretación astrofísica general

Los resultados ANOVA (sección 1, Test ANOVA) muestran que casi todas las variables tienen diferencias significativas entre clases, lo que es consistente con la existencia de poblaciones de asteroides orbital y físicamente distintas.

En particular:
- Parámetros como $\textrm{MOID}$, $a$, $e$, $D$ y $H$ son discriminantes clave, reflejando diferencias en riesgo de aproximación y composición.
- Variables de orientación ($\omega$) son menos discriminantes estadísticamente, indicando que la geometría de la órbita por sí sola no separa bien las clases.
- Las magnitudes de los estadísticos F (tabla ANOVA) sugieren que $a$, $e$, y parámetros relacionados con el riesgo ($\textrm{MOID}$) son los más separadores.
- Los gráficos orbitales (4.10.1 y 4.10.2) permiten visualizar estas diferencias en el espacio 2D y 3D, confirmando que las órbitas de distintas clases ocupan regiones distintas.

Esta separación clara motiva el uso de técnicas supervisadas para clasificar asteroides basándose en sus propiedades astrofísicas."""

            nb['cells'][i]['source'] = new_content.split('\n')
            # Ajustar los saltos de línea para el formato JSON
            nb['cells'][i]['source'] = [line + '\n' for line in new_content.split('\n')[:-1]] + [new_content.split('\n')[-1]]
            
            print("✅ Celda Interpretación Física refactorizada correctamente")
            break

# Guardar notebook
with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("\n✅ Notebook guardado correctamente")
