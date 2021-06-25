import re

text = "N1: +48 123 456 789, N2: +123 987 654 321, N3: 987 654 321, N4: 987654321"
# pattern = re.compile(r"\+\d\d \d\d\d \d\d\d \d\d\d")
pattern = re.compile(r"\+?\d{,3}[-\s]+\d{3}[-\s]+\d{3}[-\s]+\d{3}")

