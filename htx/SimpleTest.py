from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from htx.Login.steps.login import login

driver = webdriver.Firefox()
login(driver)
driver.get("https://localhost:9002/tbx/product/productedit.xhtml?id=new")
elem = driver.find_element_by_id("searchWhat")
driver.find_element_by_xpath()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "35" in driver.page_source
