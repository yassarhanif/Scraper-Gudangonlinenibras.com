import os
import pandas as pd

# Tentukan direktori induk yang berisi subfolder "HASILSCRAPE"
parent_dir = os.getcwd()
hasilscrape_dir = os.path.join(parent_dir, 'HASILSCRAPE')

# Buat list untuk menampung DataFrame dari masing-masing file
df_list = []

# Lakukan iterasi pada setiap subfolder di dalam "HASILSCRAPE"
for subdir, dirs, files in os.walk(hasilscrape_dir):
    # Lakukan iterasi pada setiap file yang ada di dalam subfolder tersebut
    for file in files:
        # Jika nama file adalah "sizewarnagambarharga.xlsx", maka gabungkan datanya
        if file == 'sizewarnagambarharga.xlsx':
            # Buat path lengkap untuk file tersebut
            file_path = os.path.join(subdir, file)
            # Baca file excel dan tambahkan ke list df_list
            df_list.append(pd.read_excel(file_path))

# Gabungkan semua DataFrame yang ada di dalam df_list
merged_df = pd.concat(df_list)

# Simpan hasil penggabungan ke folder \Scraper GON\ dengan nama file "hasilpenggabungan.xlsx"
output_file = os.path.join(os.path.dirname(parent_dir), 'hasil.xlsx')
merged_df.to_excel(output_file, index=False)
