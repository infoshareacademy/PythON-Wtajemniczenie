import re

text = """rozliczenie.txt
wyniki.txt
wakacje.jpg
pulpit.png
notatka.txt
"""
pattern = re.compile(r".*.txt")

print(pattern.findall(text))
