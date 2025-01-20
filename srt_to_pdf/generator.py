import sys
import jinja2
from pathlib import Path
from weasyprint import HTML, CSS

if (getattr(sys, 'frozen', False)):
   FILE_PATH = Path(sys.executable).parent
else:
   FILE_PATH = Path(__file__).resolve().parent.parent


# FILE_PATH = Path(__file__).resolve().parent.parent | deprecated in benefit of the above.
HTML_OUTPUT_PATH = FILE_PATH / 'OUTPUT' / 'HTML'
TEMPLATES_PATH = FILE_PATH / 'templates'
TEMPLATES_STYLE_PATH = TEMPLATES_PATH / 'styles'

def generate_html(template: str, ctx: dict, output_path: str = HTML_OUTPUT_PATH) -> None:
   """
      Generates the HTML that will be used to construct the PDF.
      It takes a template name that must exist within the templates folder and a context dictionary that matches
      the variables used in the template.
      
      @params:
         - template: str -> The name of the template file, without extension.
         - ctx: dict -> The context dictionary that will be used to render the template.
         - output_path: str -> The path where the HTML file will be saved, with extension.
   """
   
   if Path(template).suffix != '.html':
      if Path(template).is_dir():
         raise FileNotFoundError(f'{template} is a directory, must be an HTML file.')
   
   output_path = Path(output_path) # CHANGES THE TYPE OF output_path to Path
   
   env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_PATH))
   template_render = env.get_template(template + '.html')
   output = template_render.render(media=ctx, css = TEMPLATES_STYLE_PATH / (template + '.css'))
   ensure_dir(output_path.parent)
   with open(output_path, 'w') as f:
      f.write(output)

def generate_pdf(html_file: str, output_file: str, css_file:str) -> None:
   """
      Generates a PDF file from an HTML file.

      @params:
         - html_file: str -> The path to the HTML file.
         - output_file: str -> The path where the PDF file will be saved, with PDF name and extensions.
         - css_file: str -> The path of the template's CSS file.
   """
   if not Path(html_file).exists():
      raise FileNotFoundError(f'{html_file} does not exist.')
   if not Path(css_file).exists(): 
      raise FileNotFoundError(f'{css_file} does not exist.')
   
   ensure_dir(Path(output_file).parent)

   HTML(html_file).write_pdf(output_file, stylesheets=[CSS(filename=css_file)])

def ensure_dir(path: Path) -> None:
   """
      Ensures a directory exists.
   """
   if not(isinstance(path, Path)) and not(isinstance(path, str)):
      raise TypeError('Path must be a string or a Path object.')
   
   path = Path(path)

   if not path.exists():
       path.mkdir(parents=True)