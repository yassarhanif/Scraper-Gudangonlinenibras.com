import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# set up options for headless browsing
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')

# buka linkproduk.txt
with open("linkproduk.txt") as f:
    url = f.read()

# set up the webdriver and go to the target URL
driver = webdriver.Chrome(options=options)
driver.get(url)

# select dropdown for size and color
size_dropdown = driver.find_element(By.XPATH, '//*[@id="item-control"]/form/div[2]/div[5]/div/div/select')
color_dropdown = driver.find_element(By.XPATH, '//*[@id="item-control"]/form/div[2]/div[4]/div/div/select')

# get all available options for size and color
size_options = [option.get_attribute("text") for option in size_dropdown.find_elements(By.TAG_NAME, 'option')]
color_options = [option.get_attribute("text") for option in color_dropdown.find_elements(By.TAG_NAME, 'option')]

# sort the size options based on a predefined order
#size_options = sorted(size_options, key=lambda x: ['XS', 'S', 'M', 'S/M', 'L', 'XL', 'L/XL', 'XXL', 'XXXL', 'XXXXL', 'XXXXXL'].index(x))
# urutkan size
size_options = sorted(size_options, key=lambda x: (int(x) if x.isnumeric() else float('inf'), ['XS', 'S', 'M', 'S/M', 'L', 'XL', 'L/XL', 'XXL', 'XXXL', 'XXXXL', 'XXXXXL'].index(x) if x in ['XS', 'S', 'M', 'S/M', 'L', 'XL', 'L/XL', 'XXL', 'XXXL', 'XXXXL', 'XXXXXL'] else float('inf')))


# loop through all possible combinations of size and color and extract the price
with open("harga.txt", "w") as f:
    for size in size_options:
        Select(size_dropdown).select_by_visible_text(size)
        for color in color_options:
            Select(color_dropdown).select_by_visible_text(color)
            #time.sleep(1) # wait for the price to update
            price = driver.find_element(By.ID, "product-price").text.replace(",", "")
            f.write(size + ", " + color + ", " + price + "\n")

# quit the webdriver
driver.quit()
