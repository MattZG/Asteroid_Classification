@echo off
cd /d "c:\Users\matia\Asteroid_Classification"
echo Cleaning up temporary files...
del "analyze_notebook.py" 2>nul
del "cleanup.py" 2>nul
del "doc_review_corrections.py" 2>nul
del "doc_review_corrections_2.py" 2>nul
del "extract_all_notations.py" 2>nul
del "extract_notations.py" 2>nul
del "final_cleanup.py" 2>nul
del "refactor_eda_notation.py" 2>nul
del "cleanup.bat" 2>nul
echo Done
