import os

files_to_delete = [
    'analyze_notebook.py',
    'doc_review_corrections.py',
    'doc_review_corrections_2.py',
    'extract_all_notations.py',
    'extract_notations.py',
    'refactor_eda_notation.py',
    'cleanup.py'
]

for filename in files_to_delete:
    filepath = os.path.join(r'c:\Users\matia\Asteroid_Classification', filename)
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
    except Exception as e:
        pass
