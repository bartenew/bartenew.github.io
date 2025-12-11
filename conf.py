# -- Project information -----------------------------------------------------

project = "Resume"
author = "Arsenii Andriushchenko"

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",  # optional, allows Markdown if you ever add md files
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

# Favicon (your briefcase emoji)
html_favicon = (
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/"
    "thumbs/120/microsoft/209/briefcase_1f4bc.png"
)

# Clean up navigation and extra UI elements
html_theme_options = {
    "sidebar_hide_name": True,
    "navigation_with_keys": False,
    "light_logo": None,
    "dark_logo": None,
}

# Don't show "view source"
html_show_sourcelink = False

# Don't show Sphinx footer
html_show_sphinx = False
