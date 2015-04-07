from Login.TestMethods.selenium import writeById, press
from Login.environment import LOCALHOST_TBX_


def logIn(context, login="ba@nemesese.de"):
    context.driver.get(LOCALHOST_TBX_)
    writeById(context, "j_username", login)
    writeById(context, "j_password", "test1234")
    press(context, "login")


def visit(context, site):
    context.driver.get(LOCALHOST_TBX_ + site)

def siteContains(context, param):
    return param in context.driver.page_source


