import regex

REGP_TIMESTAMP = r'(^\d{2,}):([0-5][0-9]):([0-5][0-9],\d{3}$)'
REGP_TIME_INTERVAL = r'^(\d{2,}:[0-5][0-9]:[0-5][0-9],\d{3})\s-->\s(\d{2,}:[0-5][0-9]:[0-5][0-9],\d{3})$'

class ESRTParseError(Exception):
    """
        Exception raised on parsing scenarios.

        Attributes:
            message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def read_srt(filepath:str) -> list:
    """
        Reads an SRT file and returns a list of lines.
    """
    with open(filepath, 'r', encoding='utf-8-sig') as file:
        full_txt = file.read()
    lines = full_txt.splitlines()
    return lines

def parse_srt(lines: list) -> list:
    """
        Parses the SRT file into a list containing id, timestamp and lines of the block.
    """
    block = list()
    chunk = dict()
    chunk['id'] = -1
    chunk['timestamp'] = dict()
    chunk['lines'] = list()

    for line in lines:
        if len(line) == 0:
            block.append(chunk)
            chunk.clear()
            chunk['id'] = -1
            chunk['timestamp'] = dict()
            chunk['lines'] = list()
        else:
            if line.isdigit():
                pass
                chunk['id'] = int(id)
            elif len(step := get_timeinterval_block(line)) == 2:
                chunk['timestamp'] = step
                # Check match on timestamp
            elif True:
                pass
                # Check Match on Textbox
    return block

def get_timeinterval_block(block: str) -> dict:
    """
        Takes a string and checks if it's a time interval (via extract_timeinterval_chunks).
        If it is a time interval, it separes the interval and passes each to extract_timestamp_chunks.
        
         It's expected to take '00:00:23,541 --> 00:00:24,541' and return:

         {
            from: {
                hour: '00',
                minute: '00',
                second: '23,541'
            },
            until: {
                hour: '00',
                minute: '00',
                second: '24,541'
            }
         }
        
        If any of the above processes fails, returns an empty dict().
    """
    time_interval = extract_timeinterval_chunks(block)
    if len(time_interval) == 0:
        return dict()
    
    start_time = extract_timestamp_chunks(time_interval['from'])
    end_time = extract_timestamp_chunks(time_interval['until'])

    if len(start_time) == 0 ^ len(end_time) == 0:
        raise ESRTParseError('Error on parsing time interval block. Only one timestamp was found.').with_traceback()
    
    output = dict()
    output['from'] = start_time
    output['until'] = end_time

    return output


def extract_timeinterval_chunks(timeinterval: str) -> dict:
    """
        Takes a string and tries to match it against the REGP_TIME_INTERVAL. If succeeds,
        return a dict with keys 'from' and 'until'.

        It's expected to take '00:00:23,541 --> 00:00:24,541' and return:

        {
            'from':'00:00:23,541',
            'until':'00:00:24,541'
        }

        If it does not match the pattern, returns an empty dictionary.
    """
    match = regex.match(REGP_TIME_INTERVAL, timeinterval)
    
    if match:
        start_time, end_time = match.groups()
        output = {}
        output['from'] = start_time
        output['until'] = end_time
        return output
    
    return {}


def extract_timestamp_chunks(timestamp: str) -> dict:
    """
        Takes a string and tries to match it against the REGP_TIMESTAMP. If succeeds, returns
        a dict with keys 'hour', 'minute', 'second'.

        It's expected to take '00:00:23,541' and return:
        {
            'hour':'00',
            'minute':00',
            'second':'23,541'
        }

        If it does not match the pattern, returns an empty dictionary.

        - TO-DO Write functions to go from this to a dict with the same signature but the values
        as int/float. To go from values as int/floats to this signature AND to hold both.
    """
    match = regex.match(REGP_TIMESTAMP, timestamp)

    if match:
        hours, minutes, seconds = match.groups()
        output = dict()
        output['hour'] = hours
        output['minute'] = minutes
        output['second'] = seconds
        return output
    
    return {}
