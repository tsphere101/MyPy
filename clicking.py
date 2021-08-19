from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://popcat.click/")
elem = driver.find_element_by_id("app")

while True:
    elem.click()