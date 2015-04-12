from selenium.webdriver.common.by import By
from simplylocal.helper.selenium.selenium import wait

__author__ = 'christoph'


class SelectOneList:
    def __init__(self, context=None, select_id=None):
        self.select_id = select_id
        self.context = context

    def open(self):
        label = self.context.driver.find_element(By.CSS_SELECTOR, "label[id*='{0}_label']".format(self.select_id))
        label.click()
        wait(self.context)

    def select(self, element_id):
        self.open()
        label = self.context.find_element(By.CSS_SELECTOR, "div[id*='{0}]".format(self.select_id))
        label.find_element(By.XPATH, "//li[@data-label='{0}]'".format(element_id)).click()
        wait(self.context)

    def all(self):
        panel__format = "div[id$='{0}_panel']".format(self.select_id)
        return self.context.driver.find_element(By.CSS_SELECTOR,
                                                panel__format).find_elements(
            By.CSS_SELECTOR, "li")

    def elements_count(self):
        return len(self.all())

    def select_index(self, a):
        self.open()
        self.all()[a].click()
        wait(self.context)


