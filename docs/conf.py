# Configuration file for the Sphinx documentation builder.

##-- Project information

project = 'Canadian NEMO Ocean Modelling Forum Community of Practice'
#copyright = '2021, Graziella'
#author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static', '_static/_UofA', '_static/_UManitoba']

# -- Options for EPUB output
epub_show_urls = 'footnote'
