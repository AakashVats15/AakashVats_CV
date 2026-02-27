import os
import yaml
from jinja2 import Environment, FileSystemLoader

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_yaml():
    yaml_path = os.path.join(BASE_DIR, "cv_data", "cv.yaml")
    with open(yaml_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_template():
    template_dir = os.path.join(BASE_DIR, "templates")
    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True
    )
    return env.get_template("cv_template.md")

def generate_markdown():
    data = load_yaml()
    template = load_template()

    rendered_md = template.render(cv=data)

    output_path = os.path.join(BASE_DIR, "output", "cv.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered_md)

    print(f"Markdown CV generated at: {output_path}")

if __name__ == "__main__":
    generate_markdown()