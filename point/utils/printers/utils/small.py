"""

small utils

"""

import string
letter =  lambda index: string.ascii_uppercase[index]
small_margin = "\n  "
margin = "\n\t\t"
twoline = "\n\n"
paragraph = lambda array, separator = margin: separator + separator.join(array)
to_singleline = lambda m: " ".join(m.replace('\n', ' ').split()).strip()
