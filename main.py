import srt_to_pdf as s2p
from srt_to_pdf.sanitizer import sanitize_tags

#TO-DO Write an enhanced version of the parser that joins text from different timestamps that belongs to the same block
# One way to verify that is through punctuation.

def main():
    lines = s2p.read_srt('probe.srt')
    srt = s2p.complete_parse_srt(lines)
    #for block in srt:
    #    print(block)

    context = {
        'title':'Die Kaiserin',
        'subtitle':'Probe Episode',
        'blocks':srt
    }
    s2p.generate_html('template',context)

main()