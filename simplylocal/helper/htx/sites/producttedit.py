from selenium.webdriver.common.by import By
from simplylocal.helper.selenium.selenium import wait

__author__ = 'christoph'


class ProductEdit:
    def __init__(self, context):
        self.context = context

    def select_category(self, cat):
        categories = self.context.driver.find_elements(By.CSS_SELECTOR, "a[id*='category'] div[class*='select-column-content']")
        for myCat in categories:
            if myCat.text in cat:
                myCat.click()
                wait(self.context)
                return

    def all_attributes(self):
        type_ = "tbody[id='prodForm:productContent:variants_data'] label"
        attributes = self.context.driver.find_elements(By.CSS_SELECTOR, type_)
        ret = []
        for att in attributes:
            ret.append(att.text)
        type_ = "tbody[id='prodForm:productContent:variants_data'] input[id*='type']"
        attributes = self.context.driver.find_elements(By.CSS_SELECTOR, type_)
        for att in attributes:
            ret.append(att.get_attribute("value"))
        return ret


