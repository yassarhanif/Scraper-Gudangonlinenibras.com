import subprocess
import os

# Menjalankan script scraperGON.py
subprocess.run(["python", "scraperGON.py"], cwd=os.getcwd())

input("Tekan tombol enter untuk melanjutkan...")

# Tentukan direktori hasil scrape
direktori = "HASILSCRAPE"

for folder in os.listdir(direktori):
    if os.path.isdir(os.path.join(direktori, folder)):
        # Tentukan path lengkap dari folder saat ini
        current_dir = os.path.join(direktori, folder)
        # Jalankan script sizewarnagambarharga.py di dalam folder saat ini
        print('Sedang membuat file sizewarnagambarharga.xlsx pada folder ' + current_dir)
        subprocess.run(["python", "sizewarnagambarharga.py"], cwd=current_dir)

# Jalankan script gabungfileexcel.py setelah loop for selesai dijalankan
print('sedang menggabungkan sizewarnagambarharga.xlsx menjadi satu')
subprocess.run(["python", "gabungfileexcel.py"], cwd=os.getcwd())
print('Proses penggabungan sudah selesai. Cari file hasil.xlsx')