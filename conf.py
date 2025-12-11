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
html_favicon = "https://media.licdn.com/dms/image/v2/D5603AQE6qLJAzvXdZg/profile-displayphoto-shrink_200_200/B56ZVzs98XGoAY-/0/1741402924236?e=1767225600&v=beta&t=O1uInGkMDfw-BdKOhemrFHk0RWuAjXCejyfrDg6NtGs"
html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'


# Don't show "view source"
html_show_sourcelink = False

# Don't show Sphinx footer
html_show_sphinx = False
