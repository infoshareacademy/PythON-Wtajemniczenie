import re

text = "Kontaktowy numer telefonu: +48 123 456 789 (dostępny od 8:00 do 16:00)"
pattern = re.compile(r"\+\d\d \d\d\d \d\d\d \d\d\d")

text_2 = "Ala ma kota, nazywa się Mruczek i jest bardzo wesołym zwierzakiem. Mruczek ma 5 lat."
pattern_2 = re.compile(r"\d")
pattern_3 = re.compile(r"\D")
pattern_4 = re.compile(r"\s")
pattern_5 = re.compile(r"\w")
