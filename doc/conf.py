# Configuration file for the Sphinx documentation builder.
# Please don't edit: generated by nmk-doc plugin
# Contribute to "docXxx" config items in nmk.yml instead!

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Project information
project = "nmk-rust"
copyright = "2024, The dynod project"
author = "The dynod project"

# Extensions configuration
extensions = ["autoapi.extension", "myst_parser", "sphinx_rtd_theme"]

# HTML theme
html_theme = "sphinx_rtd_theme"

# Extra configuration

autoapi_dirs = ['../src']
autoapi_ignore = ['*tests*', '*templates*']
autoapi_options = ['members', 'undoc-members', 'show-inheritance', 'show-module-summary']
