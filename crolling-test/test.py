from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'MyApp/1.0')]
urllib.request.install_opener(opener)

driver = webdriver.Chrome(executable_path= r'./chromedriver')
driver.get("https://www.google.co.kr/imghp?hl=ko&authuser=0&ogbl")

elem = driver.find_element_by_name("q")
elem.send_keys("wookey")
elem.send_keys(Keys.RETURN)

driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click()
time.sleep(3)
imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
print(imgUrl)

urllib.request.urlretrieve(imgUrl, "test3.jpg")

driver.close()

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()