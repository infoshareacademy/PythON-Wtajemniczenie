import re

text = "N1: +48 123 456 789"
pattern = re.compile(r"\+(\d{2})((?: \d{3}){3})")

