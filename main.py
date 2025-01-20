import srt_to_pdf as s2p
from pathlib import Path
import fire


def do_conversion(
   srt_file: str = None,
   html_output: str = None,
   pdf_output: str = None,
   template_name: str = None,
   pdf_title: str = None,
   pdf_subtitle: str = None
   ):
    """
        Converts a subtitle SRT file to a PDF file using a template.

        Args:
            srt_file (str): The path to the SRT file.
            html_output (str): The path where the HTML file will be saved, with filename and extension.
            pdf_output (str): The path where the PDF file will be saved, with filename and extension.
            template_name (str): The name of the template file, without extension.
            pdf_title (str): The title of the PDF (presented on the heading).
            pdf_subtitle (str): The subtitle of the PDF (presented on the heading).
    """
    if not any([srt_file, html_output, pdf_output, template_name, pdf_title, pdf_subtitle]):
        raise fire.core.FireError(
        "No arguments provided. Use `--help` to view usage information."
    )
    s2p.convert_srt_to_pdf(srt_file, html_output, pdf_output, template_name, pdf_title, pdf_subtitle)

def main():  
    try:
        fire.Fire(do_conversion)
    except fire.core.FireError as e:
        fire.Fire(do_conversion, command=['--help'])


main()