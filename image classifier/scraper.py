from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request

# Set up the webdriver
driver = webdriver.Chrome()

# Navigate to Google
driver.get('https://www.google.com')

# Find the search bar and enter a query
search_bar = driver.find_element(By.NAME, 'q')
search_bar.send_keys('rockets')
search_bar.submit()

# Click on the Images tab
images_tab = driver.find_element(By.CSS_SELECTOR, '#cnt > div:nth-child(8) > div > div > div > div.TrmO7 > div > a:nth-child(2) > div')
images_tab.click()

# Scroll down to load more images
for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.implicitly_wait(2)

# Download the first 10 images
image_urls = driver.find_elements(By.XPATH, '//img[@class="rg_i"]')
for i in range(10):
    if len(image_urls) > i:
        image_url = image_urls[i].get_attribute('src')
        urllib.request.urlretrieve(image_url, f'rocket{i}.jpg')

# Close the webdriver
driver.quit()
