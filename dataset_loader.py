
import pandas as pd
from preprocessing import bersihkan_teks
from mitigasi import rekomendasi_mitigasi

# Memuat dataset CSV
def load_dataset(csv_path):
    data = pd.read_csv(csv_path)

    # Convert angka → label teks
    if data["label"].dtype != object:
        data["label"] = data["label"].map({1: "bencana", 0: "non-bencana"})

    # Tambahkan kolom mitigasi otomatis
    data["mitigasi"] = data["text"].apply(lambda x: rekomendasi_mitigasi(x)[0])

    # Bersihkan teks
    data["text"] = data["text"].apply(bersihkan_teks)

    return data
