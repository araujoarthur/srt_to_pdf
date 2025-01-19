import srt_to_pdf as s2p
from srt_to_pdf.sanitizer import sanitize_tags
from pathlib import Path

#TO-DO Write an enhanced version of the parser that joins text from different timestamps that belongs to the same block
# One way to verify that is through punctuation.

def main():
    files = Path('AImperatrizSRT/')

    # Getting the srt files list comprehension
    files = [file for file in files.iterdir() if (file.is_file() and file.suffix == '.srt')]

    for file in files:
        s2p.convert_srt_to_pdf(
            srt_file = file,
            html_output = f'OUTPUT/HTML/{file.stem}.html',
            pdf_output = f'OUTPUT/PDF/{file.stem}.pdf',
            template_html = 'template',
            template_css = 'templates/styles/template.css',
            title = 'A Imperatriz',
            subtitle = file.stem
        )


main()