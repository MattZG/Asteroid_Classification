from pathlib import Path

# Correcciones adicionales para 03_EDA.ipynb
nb_path = Path('03_Notebooks/01_Desarrollo/03_EDA.ipynb')

with open(nb_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Lista de correcciones
correcc = [
    # Sección de Asimetría y Curtosis - línea 1
    ("### 3.2 Asimetria y Curtosis", 
     "### 3.2 Asimetría y curtosis"),
     
    # Párrafo largo
    ("Utilizando medidas estadisticas como la asimetria y curtosis. La primera determina como su nombre indica mide la asimetria de la distribución en torno a la media, mientras que la segunda mide la agudeza y planitud de la distribución determinando así cuantos valores atipicos extremos tiene respecto a una distribucón normal.",
     "Utilizando medidas estadísticas como la asimetría y la curtosis. La primera, como su nombre indica, mide la asimetría de la distribución en torno a la media, mientras que la segunda mide la agudeza y planitud de la distribución, determinando así cuántos valores atípicos extremos tiene con respecto a una distribución normal."),
    
    # Sección de Skew/Shew - corregir "Shew" por "Skew" en múltiples lugares
    ("1.- Asimetria o Skew:",
     "1.- Asimetría o Skew:"),
    
    ("- Shew $\\approx$ 0 $\\rightarrow$ es simetrica la distribución",
     "- Skew $\\approx$ 0 $\\rightarrow$ la distribución es simétrica"),
    
    ("- Shew > 0 $\\rightarrow$ inclinada hacia la derecha",
     "- Skew > 0 $\\rightarrow$ inclinada hacia la derecha"),
    
    ("- Shew < 0 $\\rightarrow$ inclinada hacia la izquierda",
     "- Skew < 0 $\\rightarrow$ inclinada hacia la izquierda"),
    
    ("- Curtosis > 3 $\\rightarrow$ más outliers (más datos en las colas de la distribución)",
     "- Curtosis > 3 $\\rightarrow$ más valores extremos (más datos en las colas de la distribución)"),
    
    ("- Curtosis < 3 $\\rightarrow$ distribución mas plana",
     "- Curtosis < 3 $\\rightarrow$ distribución más plana"),
     
    ("Aplicando este test a los datos numericos se tiene que",
     "Aplicando este test a los datos numéricos se tiene que"),
    
    # Sección "Las variables se reparten" - primera línea
    ("1.- Shew $\\approx$ 0 y Curtosis < 3: **om**, **w**, **ma**, **rms** son las variables con distribución homogenea y pocos outliers\n\n2.- Shew < 0 y Curtosis > 3: **H**, **tp** y **tp_cal** tiene una tendencia hacia la izquierda junto a un número considerable de outliers\n\n3.- Shew > 0 y Curtosis > 3: **diameter**, **albedo**, **e**, **q**, **a**, **i**, **ad**, **n**, **per**, **per_y**, **moid**, **moid_ld** pertenecen al grupo de variables con tendencia hacia la derecha y altos outliers en los datos\n\nAhora seria un buen momento para hacer un conteo de los outliers por variables y tambien de tomar una decisión sobre que hacer con ellos.",
     "1.- Skew $\\approx$ 0 y Curtosis < 3: **om**, **w**, **ma**, **rms** son las variables con distribución homogénea y pocos outliers\n\n2.- Skew < 0 y Curtosis > 3: **H**, **tp** y **tp_cal** tienen una tendencia hacia la izquierda junto a un número considerable de outliers\n\n3.- Skew > 0 y Curtosis > 3: **diameter**, **albedo**, **e**, **q**, **a**, **i**, **ad**, **n**, **per**, **per_y**, **moid**, **moid_ld** pertenecen al grupo de variables con tendencia hacia la derecha y altos outliers en los datos\n\nAhora sería un buen momento para hacer un conteo de los outliers por variables y también para tomar una decisión sobre qué hacer con ellos."),
    
    ("Definiendo la función para buscar los outliers que tienen las variables numericas",
     "Se define una función para detectar los outliers en las variables numéricas"),
     
    ("La mayoria de los outliers se concentran en las varibles de tipo *sigma* que contiene la incertidumbre o error de la variable original, tal que es logico que contengan la mayor parte de ellos. Entre las variables orignales **H** libera con 2720 outliers, considerando que el dataset original tiene un total aproximado de 12000 datos, hacer una eliminación de esos 2700 datos no signifcaria un perdida grande respecto al volumen de datos.",
     "La mayoría de los outliers se concentran en las variables de tipo *sigma* que contienen la incertidumbre o error de la variable original, por lo que es lógico que contengan la mayor parte de ellos. Entre las variables originales, **H** lidera con 2.720 outliers; considerando que el dataset original tiene un total aproximado de 12.000 datos, hacer una eliminación de esos 2.700 datos no significaría una pérdida grande respecto al volumen de datos."),
    
    ("Para ver la volatividad de las variables calculamos el coeficientes de variación, que es la relación entre la desviación estandar y la media de cada variable.",
     "Para ver la volatilidad de las variables calculamos el coeficiente de variación, que es la relación entre la desviación estándar y la media de cada variable."),
    
    ("Quitando las variables *sigma*, por razones ya mencionadas. Las variables tiene poco volatividad, dado que la relación entre sus medidas estadisticas se encuentra dentro de los valores 1.70 y 0.0002. Es decir, los datos son estables y no hay mucha variación en ellos.",
     "Excluyendo las variables *sigma* por razones ya mencionadas, las variables tienen poca volatilidad, pues la relación entre sus medidas estadísticas se encuentra dentro de los valores 1,70 y 0,0002. Es decir, los datos son estables y no hay mucha variación en ellos."),
    
    ("Los resultados se encuentran enla siguiente tabla",
     "Los resultados se encuentran en la siguiente tabla"),
    
    ("El estadistico F representa la relación entre la varianza entre grupos de **class** y la varianza dentro de los grupos de la misma variable que se revisa, mientras mayor sea el valor más grande es la diferencia entre los grupos. Por su parte p-value indica la probalidad de obtener de forma aleatoria ese valor F, suponiendo que $H_{0}$ sea cierta. Tal que, si p < 0.05 se rechaza $H_{0}$ y hay un diferencia significativa entre los grupos, mientras que si p > 0.05 no se rechaza $H_{0}$ por lo tanto no hay diferencia significativa entre los grupos.",
     "El estadístico F representa la relación entre la varianza entre grupos de **class** y la varianza dentro de los grupos de la misma variable que se revisa; cuanto mayor sea el valor, mayor es la diferencia entre los grupos. El p-value indica la probabilidad de obtener aleatoriamente ese valor F suponiendo que $H_{0}$ sea cierta. Por lo tanto, si p < 0,05 se rechaza $H_{0}$ y hay una diferencia significativa entre los grupos; si p > 0,05 no se rechaza $H_{0}$ y por tanto no hay diferencia significativa entre los grupos."),
    
    ("Quitando la variable **w**, todas demás las variables tiene diferencia significativas entre los grupos definidos por la variable **class**, lo que sugiere que estan bien definidas respecto a sus caracteristicas fisicas y parametros orbitales. Esto es positivo del punto de vista del modelado, ya que implica que existen patrones que el modelo puede clasificar con mayor precisión.",
     "Excluyendo la variable **w**, todas las demás variables tienen diferencias significativas entre los grupos definidos por la variable **class**, lo que sugiere que están bien definidas respecto a sus características físicas y parámetros orbitales. Esto es positivo desde el punto de vista del modelado, ya que implica que existen patrones que el modelo puede clasificar con mayor precisión."),
]

applied_count = 0
for old, new in correcc:
    if old in content:
        content = content.replace(old, new)
        applied_count += 1
        print(f"✓ Corregido: {old[:60]}...")
    else:
        print(f"✗ NO encontrado: {old[:60]}...")

with open(nb_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ {applied_count} correcciones aplicadas de {len(correcc)} intentadas.")
