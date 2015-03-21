from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait

LOCALHOST_TBX_ = "https://192.168.1.28:9002/tbx/"

def ajax_complete(driver):
    try:
        return 0 == driver.execute_script("return jQuery.active")
    except WebDriverException:
        pass


def before_all(context):
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(10) # seconds


def after_all(context):
    context.driver.quit()