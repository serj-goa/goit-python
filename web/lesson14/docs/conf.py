import sys
import os

sys.path.insert(0, os.path.abspath(".."))

project = "lesson14"
copyright = "2023, Serhii"
author = "Serhii"

extensions = ["sphinx.ext.autodoc"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "nature"
html_static_path = ["_static"]
