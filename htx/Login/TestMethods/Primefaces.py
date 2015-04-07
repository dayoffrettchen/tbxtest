from selenium.webdriver.common.by import By

__author__ = 'christoph'

def selectManyMenuSelect(menu, label):
    for selectLabel in menu.find_elements(By.CSS_SELECTOR, "label"):
        if label in selectLabel:
            menu.find_elements(By.XPATH,"//ul/li[text()='"+label+"'").click()

# //div[@id='LNSYNDGLP0_SL_CCY_panel']/ul/li[text()='item value']
