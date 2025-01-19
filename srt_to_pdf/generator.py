import jinja2
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent.parent
HTML_OUTPUT_PATH = FILE_PATH / 'OUTPUT' / 'HTML'
TEMPLATES_PATH = FILE_PATH / 'templates'
TEMPLATES_STYLE_PATH = TEMPLATES_PATH / 'styles'

def generate_html(template: str, ctx: dict, output_path: str = HTML_OUTPUT_PATH) -> None:
   """
      Generates the HTML that will be used to construct the PDF.
      It takes a template name that must exist within the templates folder and a context dictionary that matches
      the variables used in the template.
   """
   env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_PATH))
   template_render = env.get_template(template + '.html')
   output = template_render.render(media=ctx, css = TEMPLATES_STYLE_PATH / (template + '.css'))
   ensure_dir(output_path)
   with open(output_path / 'output.html', 'w') as f:
      f.write(output)

def generate_pdf(html_file: str, output_file: str) -> None:
   pass

def ensure_dir(path: Path) -> None:
   """
      Ensures a directory exists.
   """
   if not path.exists():
       path.mkdir(parents=True)