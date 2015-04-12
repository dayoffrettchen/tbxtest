from selenium import webdriver
from selenium.webdriver.common.by import By

from simplylocal.helper.htx.login import Login
from simplylocal.helper.htx.navigation import Navigation
from simplylocal.helper.htx.python.selectonelist import SelectOneList
from simplylocal.helper.htx.sites.onlineFFO import OnlineFFO


class Context:
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Firefox()


def versand(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, "label[for*='offo']")
    for element in elements:
        if element.get_attribute('innerHTML') == 'Versand':
            return element


context = Context()
Login(context).log_in()
Navigation(context).visit_site("onlineFFO")
one_list = SelectOneList(context, "selectRetailerId")

for a in range(1, one_list.elements_count()):
    one_list.select_index(a)
    ffo = OnlineFFO(context)
    ffo.select_ffo("Versand", "true")
    ffo.save()


