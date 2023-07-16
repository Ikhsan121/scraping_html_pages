from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import os

s = Service(executable_path="C:\Development\chromedriver.exe")  # this is the path to your Chrome web driver
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--headless")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s, options=options)
driver.get("https://support.destwin.com/dokuwiki/doku.php?id=backends&do=index")
content = driver.find_element(By.ID, 'dokuwiki__content')
a_tags = content.find_elements(By.TAG_NAME, 'a')
links = []
for link in a_tags:
    links.append(link.get_attribute('href'))

# Folder to save the HTML files
folder_path = "./destwin_html_pages"  # Update the folder path

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

for i in range(len(links)):
    driver.get(links[i])
    page_source = driver.page_source
    file_name = links[i].replace("https://", "").replace("/", "--").replace("?", "--").replace("=", "--")
    # Save the page source to a file
    file_path = os.path.join(folder_path, f"{file_name}.html")  # Update the file path pattern
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(page_source)
    print(f"{file_name}.html successfully created")
    sleep(1)

