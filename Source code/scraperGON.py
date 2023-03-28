import os
import requests
from bs4 import BeautifulSoup, Comment
import csv
import re
from lxml import html
import shutil
import subprocess

print('scraperGON.py dimulai')
# Baca daftar link yang akan di-scrape dari file csv
with open('../link yang mau discrape.csv', 'r') as f:
    links = [line.strip() for line in f]

# Loop melalui setiap link dan scrape data yang dibutuhkan
for link in links:
    try:
        print('Mulai scrape ' + link)
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Ambil nama folder dari tag h4
        folder_name = soup.find('h4').text.strip()

        # Buat folder dengan nama tersebut jika belum ada
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
       
        # Ambil gambar sizepack
        sizepack_element = soup.find('img', {'class': 'sizepack-img'})
        if sizepack_element:
            img_url = sizepack_element['src']
            # Download gambar dan simpan ke dalam folder dengan nama "size pack"
            with open(folder_name + '/size pack.jpg', 'wb') as f:
                f.write(requests.get(img_url).content)
            # Simpan link sizepack ke file sizepack.txt
            with open(folder_name + '/sizepack.txt', 'w') as f:
                f.write(img_url)

        # Ambil semua link gambar dengan image id "photo-1"
        img_elements = soup.find_all('img', {'id': 'photo-1'})
        for index, img in enumerate(img_elements):
            img_url = img['src']
            # Ubah nama gambar menjadi link sumber gambar
            img_name = img_url.split('/')[-1]
            img_url = 'https://www.gudangonlinenibras.com//uploads/products/large/' + img_name
            # Download gambar dan simpan ke dalam folder
            with open(folder_name + f'/{img_name}', 'wb') as f:
                f.write(requests.get(img_url).content)
        
        # Ambil deskripsi produk dari elemen div dengan id "detail-product"
        desc_element = soup.find('div', {'id': 'detail-product'})
        desc_text = desc_element.text.strip() if desc_element else ''

        # Simpan deskripsi produk ke dalam file txt
        with open(folder_name + '/deskripsi.txt', 'w') as f:
            f.write(desc_text)

        # Ambil option dropdown untuk "color"
        color_label = soup.find('label', string='color')
        if color_label:
            # Find the select element following the label
            color_select = color_label.find_next('select')

            # Extract the options from the select element
            color_options = [option.text for option in color_select.find_all('option')]
            
            # Urutkan opsi warna secara alfabetikal
            color_options.sort()

            # Simpan daftar warna ke dalam file txt
            with open(folder_name + '/warna.txt', 'w') as f:
                f.write('\n'.join(color_options))

            # Ambil option dropdown untuk "size"
            size_label = soup.find('label', string='size')
            if size_label:
                # Find the select element following the label
                size_select = size_label.find_next('select')

                # Extract the options from the select element
                size_options = [option.text.strip() for option in size_select.find_all('option')]

                # Buat dua list baru untuk menyimpan opsi ukuran yang terdiri dari huruf dan angka
                alpha_sizes = []
                num_sizes = []

                # Loop melalui setiap opsi "size" dan tambahkan ke list yang sesuai
                for size in size_options:
                    if any(x.isalpha() for x in size):
                        if size in ('S/M', 'L/XL'):
                            alpha_sizes.append(size)
                        elif size.isalpha():
                            if size in ('XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL', 'XXXXL', 'XXXXXL'):
                                alpha_sizes.append(size)
                    elif size.isnumeric():
                        num_sizes.append(int(size))

                # Urutkan list ukuran yang terdiri dari huruf menggunakan urutan yang telah didefinisikan secara manual
                alpha_sizes.sort(key=lambda x: ('XS', 'S', 'M', 'S/M', 'L', 'XL', 'L/XL', 'XXL', 'XXXL', 'XXXXL', 'XXXXXL').index(x) if x in ('XS', 'S', 'M', 'S/M', 'L', 'XL', 'L/XL', 'XXL', 'XXXL', 'XXXXL', 'XXXXXL') else float('inf'))

                # Urutkan list ukuran yang terdiri dari angka dengan menggunakan sorted()
                num_sizes = sorted(num_sizes)

                # Gabungkan kedua list yang telah diurutkan kembali menjadi satu list yang berisi semua opsi ukuran
                sorted_sizes = alpha_sizes + [str(size) for size in num_sizes]

                # Simpan daftar ukuran ke dalam file txt
                with open(folder_name + '/ukuran.txt', 'w') as f:
                    f.write('\n'.join(sorted_sizes))

        '''        
        # Ambil harga
        # membuat objek lxml untuk parsing halaman web
        tree = html.fromstring(page.content)

        # mencari elemen dengan XPath tertentu dan mengambil elemennya
        element = tree.xpath('//*[@id="item-control"]/form/div[2]/comment()[2]')[0]

        # menghapus karakter <!-- dan -->
        element_text = element.text.strip()
        element_text = element_text.replace('<!--', '').replace('-->', '')

        # membuat objek lxml untuk parsing teks HTML yang telah diubah
        element_tree = html.fromstring(element_text)

        # mencari elemen select di dalam element_tree
        select_element = element_tree.xpath('//select')[0]

        # membuat daftar harga untuk ditulis ke dalam file
        harga_list = []
        for option in select_element.xpath('.//option'):
            harga_list.append(option.text + ', ' + option.get('data-var-price'))
        
        if len(harga_list) == len(color_options) * len(sorted_sizes):
            # membuka file harga.txt untuk ditulis
            with open(folder_name + '/harga.txt', 'w') as f:
                f.write('\n'.join(harga_list))
                        
            # Menyalin file size warna gambar harga.py ke folder yang sama dengan file warna.txt
            shutil.copy('sizewarnagambarharga.py', folder_name)
                
        else:
            print(folder_name + ' mengeksekui seleniumharga.py')
            shutil.copy('sizewarnagambarharga.py', folder_name)
            shutil.copy('seleniumharga.py', os.path.join(os.getcwd(), folder_name))
            
            # Simpan link produk ke dalam file txt
            with open(folder_name + '/linkproduk.txt', 'w') as f:
                f.write(link)
            
            subprocess.run(["python", "seleniumharga.py"], cwd=folder_name)
        '''
        # membuat harga.txt dengan selenium       
        print(folder_name + ' mengeksekui seleniumharga.py')
        shutil.copy('sizewarnagambarharga.py', folder_name)
        shutil.copy('seleniumharga.py', os.path.join(os.getcwd(), folder_name))
        
        # Simpan link produk ke dalam file txt
        with open(folder_name + '/linkproduk.txt', 'w') as f:
            f.write(link)
            
        subprocess.run(["python", "seleniumharga.py"], cwd=folder_name)
            
        
    except Exception as e:
        print(f"Terjadi kesalahan saat melakukan scraping pada link {link}: {str(e)}")    
        
# Menggabungkan semua folder menjadi satu folder
source_folder = os.getcwd()
target_folder = os.path.join(source_folder, 'HASILSCRAPE')

if not os.path.exists(target_folder):
    os.makedirs(target_folder)

for folder_name in os.listdir(source_folder):
    if os.path.isdir(folder_name) and folder_name != 'HASILSCRAPE':
        source_path = os.path.join(source_folder, folder_name)
        target_path = os.path.join(target_folder, folder_name)
        shutil.move(source_path, target_path)

print('Tahap 1: Scrape GON sudah berhasil')
print('Tahap 2: Lakukan ini secara manual ->> Sortir gambar yang ingin diupload ke Tiktok. Masuk ke folder "Source Code/HASILSCRAPE/" lalu pilih 8 gambar yang ingin diupload ke tiktok. Maksimal 8 gambar dan tidak boleh lebih')