from datetime import datetime

class EMissingParam(Exception):
   """
      Exception raised when an expected **kwargs argument is missing.

      Attributes:
         message -- explanation of the error
   """

   def __init__(self, message):
      self.message = message
      super().__init__(self.message)

class EConfusingValueTypes(Exception):
   """
      Exception raised when a value is expected to be of a certain type, but it is not.

      Attributes:
            message -- explanation of the error
   """

   def __init__(self, message):
      self.message = message
      super().__init__(self.message)

def merge_lines(srt: list) -> str:
   """
      Takes the list of lines from a SRT entry structure and merges them into a single string.
   """

   return ' '.join(srt['lines'])

def simplified_chunk_transform(srt_entry: dict) -> dict:
   """
      Transforms a parsed SRT entry into a simplified one.
   """
   return {
       'id': srt_entry['id'],
       'timestamp': srt_entry['timestamp'],
       'text': merge_lines(srt_entry)
   }

def numeric_timestamp_transform(timestamp: dict) -> dict:
   """
      Transforms a timestamp from a string to a numeric value.
   """
   for key in timestamp:
       timestamp[key] = float(timestamp[key].replace(',', '.'))

   return timestamp

def numeric_timeinterval_transform(timeinterval: dict) -> dict:
   """
      Transforms a timeinterval from a string to a numeric value.
   """
   for key in timeinterval:
       timeinterval[key] = numeric_timestamp_transform(timeinterval[key])

   return timeinterval

def string_timestamp_transform(timestamp: dict) -> str:
   """
      Transforms a timestamp from a numeric value to a string.
   """
   print(timestamp)
   for key in timestamp:
       timestamp[key] = str(timestamp[key]).replace('.', ',')

   return f'''{timestamp['hour']}:{timestamp['minute']}:{timestamp['second']}'''

def time_timestamp_transform(**kwargs) -> datetime:
   """
      Transforms a timestamp from a numeric value to a datetime object.
   """

   if not ('hour' in kwargs and 'minute' in kwargs and 'second' in kwargs):
       raise EMissingParam("Missing required parameters: hour, minute, second.")
   
   timestamp = {
         'hour': kwargs['hour'],
         'minute': kwargs['minute'],
         'second': kwargs['second']
   }

   consistent_type = isinstance(kwargs['hour'], int) or isinstance(kwargs['hour'], float) or isinstance(kwargs['hour'], str)
   for _,v in timestamp.items():
      consistent_type = consistent_type and isinstance(v, type(kwargs['hour']))
   
   if not consistent_type:
      raise EConfusingValueTypes("The values of the timestamp are of different types.")
   
   
   return datetime.strptime(string_timestamp_transform(timestamp).replace(',','.'), '%H:%M:%S.%f')