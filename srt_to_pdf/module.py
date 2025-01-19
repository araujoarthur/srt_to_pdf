from .parser import read_srt, raw_parse_srt, complete_parse_srt
from .generator import generate_html, generate_pdf
from pathlib import Path

def convert_srt_to_pdf(srt_file: str, html_output: str, pdf_output:str, template_html: str, template_css: str, title:str, subtitle:str, **kwargs) -> None:
   """
      Converts an SRT file to a PDF file.
   """

   srt_lines = read_srt(srt_file)
   parsed_srt = complete_parse_srt(srt_lines)
   context = {
      'title': title,
      'subtitle': subtitle,
      'blocks': parsed_srt
   }

   generate_html(template_html, context, html_output)
   generate_pdf(html_output, pdf_output, template_css)

   print(f'Success converting {Path(pdf_output).stem}.')
