#  Zmodyfikuj dopasowywanie adresu strony internetowej tak aby:
#     1. Część z protokołem (http albo https) mogła wystąpić opcjonalnie
#     2. Za pomocą grup dopasować: protokół i nazwę strony

import re

matching_examples = ["https://www.PyJazz.pl", "http://www.pyjazz.com", "www.pyjazz.pl"]
pattern = re.compile(r"(?:(http|https)://)?www\.(\w+)\.\w+")

