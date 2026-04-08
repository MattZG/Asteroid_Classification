import json
from pathlib import Path

nb_path = Path('03_Notebooks/01_Desarrollo/03_EDA.ipynb')
with open(nb_path) as f:
    nb = json.load(f)

print("EXTRAYENDO NOTACIONES DEL NOTEBOOK\n")
print("="*60)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        content = ''.join(cell['source'])
        # Buscar celdas con LaTeX notation o con $
        if 'Notación' in content or ('$' in content and i < 20):
            print(f"\nCELDA {i}:")
            print(content[:1000])
            if len(content) > 1000:
                print("... [truncado]")
            print("-"*60)

# Mostrar también la Interpretación Física
print("\n\nBUSCANDO INTERPRETACIÓN FÍSICA:\n")
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        content = ''.join(cell['source'])
        if 'Interpretación Física' in content or 'Astro Físico' in content:
            print(f"\nCELDA {i}:")
            print(content[:1500])
            print("-"*60)
