from selenium.webdriver.common.by import By

from simplylocal.helper.selenium.selenium import select, wait


__author__ = 'christoph'


class CheckBox:
    def __init__(self, checkbox, context):
        self.context = context
        self.ffo = context.driver.find_element(By.XPATH, "//table[@id='" + checkbox + "']")

    def input(self, label):
        attribute = self.label(label).get_attribute('for')
        return self.ffo.find_element(By.XPATH, "//input[@id='" + attribute + "']")

    def label(self, label):
        return self.ffo.find_element(By.XPATH, "//label[text()='" + label + "']")

    def select(self, label, check):
        wait(self.context)
        self_label = self.label(label)
        select(self.input(label), self_label, check)

    def is_selected(self, label):
        wait(self.context)
        return self.input(label).is_selected()
