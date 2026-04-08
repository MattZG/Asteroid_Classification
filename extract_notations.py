import json

nb = json.load(open('03_Notebooks/01_Desarrollo/03_EDA.ipynb'))

# Extraer notaciones
notaciones = []
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        content = ''.join(cell['source'])
        if 'Notación LaTeX' in content or '$' in content and i < 20:
            print(f"\n=== CELL {i} ===")
            print(content[:800])
            print("---")
