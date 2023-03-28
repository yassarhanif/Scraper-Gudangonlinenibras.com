# Baca nilai variable ukuran dari file ukuran.txt
with open("ukuran.txt") as f:
    ukuran = f.read().splitlines()

# Baca nilai variable warna dari file warna.txt
with open("warna.txt") as f:
    warna = f.read().splitlines()

# Buat list kosong untuk menampung kombinasi ukuran dan warna
kombinasi = []

# Lakukan perulangan untuk membuat kombinasi ukuran dan warna
for a in ukuran:
    for w in warna:
        kombinasi.append(str(a) + ", " + w +", \n")

# Tulis kombinasi ukuran dan warna ke file hargabackup.txt
with open("harga.txt", "w") as f:
    f.writelines(kombinasi)
