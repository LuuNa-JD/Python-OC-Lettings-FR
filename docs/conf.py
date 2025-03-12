import os
import sys

sys.path.insert(0, os.path.abspath(".."))

on_rtd = os.environ.get("READTHEDOCS") == "True"

if not on_rtd:
    import django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
    django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python-OC-Lettings-JD'
copyright = '2025, Denizot Julien'
author = 'Denizot Julien'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinxcontrib_django',
    'sphinx.ext.viewcode',
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_member_order = 'bysource'
napoleon_google_docstring = True
napoleon_numpy_docstring = True


language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 4,
}
