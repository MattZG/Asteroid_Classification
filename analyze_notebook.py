#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from pathlib import Path

# Cargar notebook EDA
nb_path = Path('03_Notebooks/01_Desarrollo/03_EDA.ipynb')
with open(nb_path, encoding='utf-8') as f:
    nb = json.load(f)

# Almacenar notaciones por sección
stat_notations = {}  # Estadístico
astro_notations = {}  # Astrofísico

print("EXTRAYENDO NOTACIONES DEL NOTEBOOK EDA\n")
print("="*70)

# Buscar todas las celdas con LaTeX
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        content = ''.join(cell['source'])
        
        # Mostrar primeras 20 celdas markdown para análisis
        if i < 40:
            if '$' in content:
                print(f"\n📝 CELDA {i} (contiene LaTeX):")
                print(content[:600])
                if len(content) > 600:
                    print("...[continúa]")

print("\n" + "="*70)
print("\nAhora voy a extraer notaciones específicas:")
