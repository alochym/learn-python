# https://www.amazon.com/dp/B0BP9SNVH9

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from bs4 import Tag
from bs4 import NavigableString

import sys

userAgent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.40"

chrome_options = Options()
chrome_options.add_argument("headless")
chrome_options.add_argument(userAgent)

chrome_driver = "/opt/learn/google-chrome-webdriver/chromedriver"
svc = Service(executable_path=chrome_driver)

driver = webdriver.Chrome(options=chrome_options, service=svc)

# url = "https://www.amazon.com/dp/B0BP9SNVH9"
url = sys.argv[1]
driver.get(url)

driver.execute_script("return navigator.userAgent")

# all content of HTML Document
page_source = driver.page_source
# print(page_source)

soup = BeautifulSoup(page_source, "lxml")

# All Info of Product
product = soup.find_all("div", {"id": "centerCol"})[0]

name = product.find_all("div", {"id": "title_feature_div"})[0].div.h1.span.text.strip()
print(name)

price = product.find_all("div", {"id": "apex_desktop"})[0].find_all("span", "a-offscreen")[0].text.strip()
print(price)

# product_band = product.find("a", {"id": "bylineInfo"}).string



