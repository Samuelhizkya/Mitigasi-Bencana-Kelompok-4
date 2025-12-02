# ===============================
import time
from tabulate import tabulate
from colorama import Fore, init

from dataset_loader import load_dataset
from model_training import train_model
from twitter_api import ambil_tweet
from preprocessing import bersihkan_teks
from mitigasi import rekomendasi_mitigasi

init(autoreset=True)

# ==== LOAD DATASET ====
dataset_path = r"C:\samuel\belajar\mitigasi full\dataset_bencana_indonesia.csv"
data = load_dataset(dataset_path)

# ==== TRAIN MODEL ====
model, vectorizer, accuracy = train_model(data)

# ==== MENU PROGRAM ====
def main():
    while True:
        print(Fore.GREEN + "\n═══════════════════════════════════════")
        print(" 🚨 SISTEM MITIGASI BENCANA AI — MENU ")
        print("═══════════════════════════════════════")
        print("1. Ambil Data dari Twitter API / CSV")
        print("2. Input Manual Kalimat")
        print("3. Keluar")

        pilihan = input("\nPilih Menu (1/2/3): ")

        if pilihan == "3":
            print("Terima kasih 🙏")
            break

        if pilihan == "1":
            tweets, sumber = ambil_tweet()

            # fallback jika API error
            if tweets is None:
                print(Fore.YELLOW + "\n⚠ API LIMIT → Ambil 10 data dari dataset")
                tweets = data.sample(10)["text"].tolist()
                sumber = "DATASET CSV"

        elif pilihan == "2":
            kalimat = input("Masukkan kalimat: ")
            tweets = [kalimat]
            sumber = "INPUT MANUAL"

        else:
            print(Fore.RED + "❌ Pilihan tidak valid!")
            continue

        # ==== TABEL AWAL ====
        print(Fore.CYAN + "\n📥 DATA YANG DIKLASIFIKASI")
        tampil_awal = [[i+1, t[:90]] for i, t in enumerate(tweets)]
        print(tabulate(tampil_awal, headers=["No", "Tweet"], tablefmt="grid"))

        time.sleep(1)

        # ==== KLASIFIKASI ====
        clean = [bersihkan_teks(t) for t in tweets]
        vec = vectorizer.transform(clean)
        hasil = model.predict(vec)

        hasil_tabel = []
        for i in range(len(tweets)):
            mitigasi, risiko = rekomendasi_mitigasi(tweets[i])
            hasil_tabel.append([
                i+1,
                tweets[i],
                hasil[i],
                risiko,
                mitigasi
            ])

        print(Fore.CYAN + "\n📊 HASIL KLASIFIKASI & MITIGASI")
        print(tabulate(hasil_tabel,
                       headers=["No", "Tweet", "Status", "Risiko", "Mitigasi"],
                       tablefmt="fancy_grid"))

        print(Fore.GREEN + f"\nAkurasi Model: {accuracy:.2f}%")
        print("Sumber Data :", sumber)

        input("\nTekan ENTER untuk kembali ke menu...")

# ==== JALANKAN ====
if __name__ == "__main__":
    main()
