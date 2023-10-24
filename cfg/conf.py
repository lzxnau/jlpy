# -- Source path setup -------------------------------------------------------
import os
import sys

sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
project = 'JLPy'
copyright = '2023, JLPy'
author = 'JLPy'
release = '2023.10.24'
version = '2023.10.24.4'

# -- General configuration ---------------------------------------------------
extensions = [
  'sphinx.ext.autodoc',
  'sphinx.ext.autosummary',
]

templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
