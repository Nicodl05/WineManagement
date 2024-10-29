import sys
import os
import pytest

# Ajouter `src` au PYTHONPATH pour que pytest puisse le trouver
sys.path.insert(0, os.path.abspath("src"))

# Exécuter pytest pour le dossier `tests`
pytest.main(["tests"])
