# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import shutil

from dibisoplot._version import __version__

sys.path.insert(0, os.path.abspath(os.path.join('..')))

# -- Project information -----------------------------------------------------

project = 'DiBISO plot'
copyright = '2025, Romain THOMAS, GPLv3'
author = 'Romain THOMAS'

# The full version, including alpha/beta/rc tags
# release = '0'
release = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    # "sphinx_rtd_theme",
    "sphinx_design",
    "nbsphinx",
    # "IPython.sphinxext.ipython_console_highlighting",
    # "IPython.sphinxext.ipython_directive",
    "sphinx_needs",
    "sphinxcontrib.test_reports",
    "sphinx_mdinclude",
]

nbsphinx_execute = "never"  # Skip execution if not needed
nbsphinx_allow_errors = True  # Allow build to continue despite JS errors
nbsphinx_remove_tagged_cells = True
nbsphinx_prompt_width = "0px"  # Hide input prompts entirely

autosummary_generate = False  # Set to False to prevent generating separate files

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'README.md',
    'notebooks/README.md',
    'notebooks/*.rst',
    '**.ipynb_checkpoints'
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
html_theme = "pydata_sphinx_theme"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html_css_files = ['notebooks.css']

# https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/web-components.html
copybutton_selector = ":not(.prompt) > div.highlight pre"
# nbsphinx_execute = "never"

# specify to not skip the init function
# https://stackoverflow.com/questions/5599254/how-to-use-sphinxs-autodoc-to-document-a-classs-init-self-method
def skip(app, what, name, obj, would_skip, options):
    if name == "__init__":
        return False
    return would_skip

def setup(app):
    app.connect("autodoc-skip-member", skip)
    # app.add_js_file("https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.6/require.min.js")

    # manually copy notebook figures
    src = os.path.join(os.path.dirname(__file__), 'notebooks', 'figures')
    dest = os.path.join(app.outdir, '_static', 'figures')
    if os.path.exists(src):
        shutil.copytree(src, dest, dirs_exist_ok=True)
