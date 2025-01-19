import srt_to_pdf as s2p
from srt_to_pdf.sanitizer import sanitize_tags

def main():
    lines = s2p.read_srt('probe.srt')
    srt = s2p.raw_parse_srt(lines)
    #for block in srt:
    #    print(block)

    print(s2p.time_timestamp_transform(**srt[-1]['timestamp']['from']))

main()