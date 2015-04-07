from selenium import webdriver

# LOCALHOST_TBX_ = "https://192.168.1.28:9002/tbx/"
LOCALHOST_TBX_ = "https://localhost:9002/tbx/"


def before_all(context):
    context.driver = webdriver.Firefox()


def after_all(context):
    context.driver.quit()