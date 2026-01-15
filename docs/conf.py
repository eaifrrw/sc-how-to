# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ICTP-EAIFR Cluster User Guide'
copyright = '2026, Edward Ntim Gasu, Ph.D, M.HPC'
author = 'Edward Ntim Gasu, Ph.D, M.HPC'
release = '0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Allow .md files
extensions = ["myst_parser"]
html_theme = "sphinx_rtd_theme"
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

