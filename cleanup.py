import os
import glob
from pathlib import Path

# Cambiar al directorio del proyecto
os.chdir(r'c:\Users\matia\Asteroid_Classification')

# Listar archivos Python en la raíz
py_files = glob.glob('*.py')
print("Archivos Python encontrados:")
for f in py_files:
    print(f"  - {f}")

# Archivos temporales a eliminar
temp_files = [
    'analyze_notebook.py',
    'doc_review_corrections.py',
    'doc_review_corrections_2.py',
    'extract_all_notations.py',
    'extract_notations.py',
    'refactor_eda_notation.py'
]

print("\nEliminando archivos temporales...")
for f in temp_files:
    if os.path.exists(f):
        os.remove(f)
        print(f"✓ {f} eliminado")
    else:
        print(f"✗ {f} no encontrado")

print("\nArchivos Python restantes:")
py_files_after = glob.glob('*.py')
for f in py_files_after:
    print(f"  - {f}")

if len(py_files_after) == 0:
    print("  (ninguno)")
