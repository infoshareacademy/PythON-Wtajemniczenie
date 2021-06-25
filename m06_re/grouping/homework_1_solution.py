# Napisz wyrażenie regularne dopasowujące polski kod pocztowy (dwie cyfry, myślnik, trzy cyfry).
# Wykorzystaj grupy by oddzielnie dopasować część dotyczącą regionu/obszaru (pierwsze dwie cyfry)
# oraz szczegóły kodu (pozostałe trzy cyfry)

import re


text = "12-456"
pattern = re.compile(r"(\d{2})-(\d{3})")
