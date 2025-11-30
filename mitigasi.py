def rekomendasi_mitigasi(tweet):
    t = tweet.lower()

    if "gempa" in t:
        return "Evakuasi ke area terbuka & jauhi bangunan", "TINGGI"

    elif "banjir" in t:
        return "Matikan listrik & pindah ke tempat tinggi", "TINGGI"

    elif "longsor" in t:
        return "Hindari lereng dan jalur rawan", "SEDANG"

    elif "kebakaran" in t:
        return "Gunakan APAR & hubungi pemadam", "TINGGI"

    else:
        return "Pantau informasi resmi BPBD", "RENDAH"
