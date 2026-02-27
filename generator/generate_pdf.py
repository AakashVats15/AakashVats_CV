import os
import yaml
import pdfkit
from jinja2 import Environment, FileSystemLoader

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_yaml():
    yaml_path = os.path.join(BASE_DIR, "cv_data", "cv.yaml")
    with open(yaml_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_template():
    template_dir = os.path.join(BASE_DIR, "templates")
    env = Environment(loader=FileSystemLoader(template_dir))
    return env.get_template("cv_template.html")

def generate_pdf():
    data = load_yaml()
    template = load_template()

    rendered_html = template.render(cv=data)

    html_path = os.path.join(BASE_DIR, "output", "cv_temp.html")
    pdf_path = os.path.join(BASE_DIR, "output", "cv.pdf")

    # Save temporary HTML
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(rendered_html)

    # Path to wkhtmltopdf executable
    wkhtml_path = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

    config = pdfkit.configuration(wkhtmltopdf=wkhtml_path)

    pdfkit.from_file(html_path, pdf_path, configuration=config)

    print(f"PDF CV generated at: {pdf_path}")

if __name__ == "__main__":
    generate_pdf()