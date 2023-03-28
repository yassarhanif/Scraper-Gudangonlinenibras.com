This code is made by chatgpt 3 using python.

What you need:
- Windows PC
- Python installed in PC
- Python library:
    - Selenium
    - BeautifulSoup
    - shutil
    - subprocess
    - openpyxl
    - pandas
    - (In case I forget to mention, please see the error at your terminal and install the library by your self ;-) )
    
===================================

How to use the script:

1. Fill the 'link yang mau discrape.csv' with product link from gudangonlinenibras.com (example: https://gudangonlinenibras.com/products/14105-itu-white-series-j).

2. Run the code by double click "MULAI SCRAPING.bat". Wait until the process done.

3. Once it's half done, you will get this message:
    "Tahap 1: Scrape GON sudah berhasil"
    "Tahap 2: Lakukan ini secara manual ->> Sortir gambar yang ingin diupload ke Tiktok. Masuk ke folder "Source Code/HASILSCRAPE/" lalu pilih 8 gambar yang ingin diupload ke tiktok. Maksimal 8 gambar dan tidak boleh lebih"
    (If you don't understand Bahasa Indonesia, please use online translator.)
    
4. After those messages appear, you can see the result inside folder "Source Code/HASILSCRAPE". At this stage, you can leave up to 8 images and delete the rest of it if you want to upload to Tiktok Shop, Shopee, and any other marketplace. But if you want to keep them, no need to delete the images.

5. Once you sorted the image, press enter in the terminal.

6. After the code finish running, you can see "hasil.xlsx" in main folder. This file contain description, size, color, variation, headline, image link url, etc. Basically stuff you need for mass upload to marketplace like Shopee, Tiktok shop, Lazada, etc. You just need to adjust the column based on each marketplace preference.

Thats all. Enjoy!
