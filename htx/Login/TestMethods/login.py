from selenium.webdriver.common.keys import Keys
from htx.Login.TestMethods.selenium import wait, writeById, press
from htx.Login.environment import LOCALHOST_TBX_


def logIn(context, login="ba@nemesese.de"):
    context.driver.get(LOCALHOST_TBX_)
    writeById(context, "j_username", login)
    writeById(context, "j_password", "test1234")
    press(context, "login")


def visit(context, site):
    context.driver.get(LOCALHOST_TBX_ + site)

def siteContains(context, param):
    return param in context.driver.page_source


