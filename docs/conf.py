# Configuration file for the Sphinx documentation builder.

project = 'scrapery'
copyright = '2025, Ramesh Chandra'
author = 'Ramesh Chandra'
release = '0.0.9'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
]

autodoc_default_options = {
    'members': True,
    'undoc-members': False,
    'private-members': False,
    'show-inheritance': True,
}

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

templates_path = ['_templates']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

import os
import sys
sys.path.insert(0, os.path.abspath('../scrapery'))
