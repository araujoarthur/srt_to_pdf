import regex

REGEP_ALL_TAGS = r'(<\/?[^>]+>)*' # This
REGEP_TAG_EXCLUSIVE = r'^(<[^>]+>)$'
REGEP_INCLUDE_TAG = r'(<[^>]+>)'

class EInvalidTag(Exception):
    """
        Exception raised on sanitization scenarios when a tag is invalid.

        Attributes:
            message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def sanitize_tags(string: str) -> str:
   """
      Sanitizes a string from tags.
   """
   match = regex.sub(REGEP_ALL_TAGS, '', string)
   
   return match


def remove_tag(string: str, tag: str) -> str:
   """
      Removes a tag from a string.
   """

   if not is_tag(tag):
       raise EInvalidTag(f"{tag} is an invalid tag.")
   
   match = regex.sub(tag, '', string)

   return match
   

def is_tag(string: str, tag: str) -> bool:
   """
      Checks if a string is a tag.
   """
   match = regex.match(REGEP_TAG_EXCLUSIVE, string)
   
   return match is not None


def include_tag(string:str) -> bool:
   """
      Includes a tag in a string.
   """
   match = regex.match(REGEP_INCLUDE_TAG, string)
   
   return match is not None