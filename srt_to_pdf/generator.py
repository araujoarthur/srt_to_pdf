import jinja2
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent.parent
HTML_OUTPUT_PATH = FILE_PATH / 'OUTPUT' / 'HTML'
TEMPLATES_PATH = FILE_PATH / 'templates'
TEMPLATES_STYLE_PATH = TEMPLATES_PATH / 'styles'

def generate_html(template: str, ctx: dict) -> None:
   """
      Generates the HTML that will be used to construct the PDF.
      It takes a template name that must exist within the templates folder and a context dictionary that matches
      the variables used in the template.
   """
   env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_PATH))
   template_render = env.get_template(template + '.html')
   output = template_render.render(media=ctx, css = TEMPLATES_STYLE_PATH / (template + '.css'))
   ensure_dir(HTML_OUTPUT_PATH)
   with open(HTML_OUTPUT_PATH / 'output.html', 'w') as f:
      f.write(output)

def

def ensure_dir(path: Path) -> None:
   if not path.exists():
       path.mkdir(parents=True)