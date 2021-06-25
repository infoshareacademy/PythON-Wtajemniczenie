# 2. Zmodyfikuj dopasowywanie adresu email tak aby:
#   1. Dopuszczać kropki w rozszerzeniu domeny
#   2. Za pomocą grup dopasować: nazwę, domenę, rozszerzenie domeny

import re

text = "nazwa@domena.com.pl"

pattern = re.compile(r"(\w+)@(\w+)((?:\.\w+)+)")

