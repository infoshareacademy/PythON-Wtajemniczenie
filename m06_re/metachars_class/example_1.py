import re

text = "Ala ma kota, nazywa się Mruczek i jest bardzo wesołym zwierzakiem."
pattern = re.compile(r"[abc]")
pattern_2 = re.compile(r"[abc.]")
pattern_3 = re.compile(r"[^a]")

