import re

text = "+48 123 456 789 oraz +48 987 654 321"
pattern = re.compile(r"\+\d\d \d\d\d \d\d\d \d\d\d")

text_2 = "Witaj! Miło Cię poznać."
text_3 = "Cześć! Co słychać?"
text_4 = "Hej! Co słychać?"
pattern_2 = re.compile(r"Witaj|Cześć")
