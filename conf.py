# -- Project information -----------------------------------------------------

project = "Resume"
author = "Arsenii Andriushchenko"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx_design"
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# We only use reStructuredText files
source_suffix = {
    ".rst": "restructuredtext",
}

# -- HTML output -------------------------------------------------------------

html_theme = "furo"   # clean and minimalist for resumes
html_title = "Arsenii Andriushchenko – Resume"

# Optional folders
html_static_path = ["_static"]
html_css_files = ["resume.css"]

# Favicon (your briefcase emoji)
html_favicon = (
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/"
    "thumbs/120/microsoft/209/briefcase_1f4bc.png"
)
html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'


# Don't show "view source"
html_show_sourcelink = False

# Don't show Sphinx footer
html_show_sphinx = False
