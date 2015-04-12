from selenium.webdriver.common.by import By

__author__ = 'christoph'


def select_many_menu_select(menu, label):
    for selectLabel in menu.find_elements(By.CSS_SELECTOR, "label"):
        if label in selectLabel:
            menu.find_elements(By.XPATH, "//ul/li[text()='" + label + "'").click()


def all_menu_items(context, element_id=""):
    elements = context.driver.find_elements(By.CSS_SELECTOR, "div[id$='" + element_id + "_panel']")
    if len(elements) > 1:
        return
    ret = []
    items = select_many_menu_items(elements[0])
    for item in items:
        ret.append(item.get_attribute("innerHTML"))
    return ret


def select_many_menu_items(menu):
    return menu.find_elements(By.CSS_SELECTOR, "li")
