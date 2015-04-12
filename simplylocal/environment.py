from configparser import ConfigParser

from selenium import webdriver


section = "localhost"


def config_map():
    dict1 = {}
    config = ConfigParser()
    config.read("simplylocal/config.ini")
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


def before_all(context):
    context.driver = webdriver.Firefox()


def after_all(context):
    context.driver.quit()