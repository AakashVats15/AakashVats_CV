import os

BASE_PATH = r"E:\Personal\GitHub\Python Code Repo\AakashVats"

folders = [
    "cv_data",
    "templates",
    "generator",
    "output",
    "tests",
    "scripts"
]

files = {
    "cv_data/cv.yaml": "# Your CV data in YAML format\n",
    "templates/cv_template.html": "<!-- HTML CV Template -->\n",
    "templates/cv_template.tex": "% LaTeX CV Template\n",
    "templates/cv_template.md": "# Markdown CV Template\n",
    "generator/__init__.py": "",
    "generator/generate_html.py": "def generate_html():\n    pass\n",
    "generator/generate_pdf.py": "def generate_pdf():\n    pass\n",
    "generator/generate_markdown.py": "def generate_markdown():\n    pass\n",
    "output/.gitkeep": "",
    "tests/test_cv_generation.py": "def test_generation():\n    assert True\n",
    "scripts/build_all.py": "def build_all():\n    pass\n",
    "README.md": "# Code-Based CV for Aakash Vats\n",
    "requirements.txt": "jinja2\npyyaml\n"
}

def create_repo():
    print(f"Creating repo at: {BASE_PATH}")

    # Create folders
    for folder in folders:
        path = os.path.join(BASE_PATH, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Created folder: {path}")

    # Create files
    for file_path, content in files.items():
        full_path = os.path.join(BASE_PATH, file_path)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created file: {full_path}")

    print("Repository structure created successfully.")

if __name__ == "__main__":
    create_repo()