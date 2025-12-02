import re

def bersihkan_teks(teks):
    teks = teks.lower()
    teks = re.sub(r"http\S+", "", teks)
    teks = re.sub(r"[^a-zA-Z\s]", "", teks)
    return teks.strip()
