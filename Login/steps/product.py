from behave import *
from selenium.webdriver.common.by import By

from Login.TestMethods.selenium import wait, allMenuItems
from Login.steps.navigation import visitSite


use_step_matcher("re")


def get_categories(category):
    return category.split('>')
    pass


def select_category(context, cat):
    categories = context.driver.find_elements(By.CSS_SELECTOR, "a[id*='category'] div[class*='select-column-content']")
    for myCat in categories:
        if myCat.text in cat:
            myCat.click()
            wait(context)
            return
    pass


@step('the category "(?P<category>.*)" is selected')
def step_impl(context, category=None):
    """
    :type context behave.runner.Context
    """
    visitSite(context, "productedit", {'id': 'new'})
    categories = get_categories(category)
    for cat in categories:
        select_category(context, cat)
    pass


def all_attributes(context):
    type_ = "tbody[id='prodForm:productContent:variants_data'] label"
    attributes = context.driver.find_elements(By.CSS_SELECTOR, type_)
    ret = []
    for att in attributes:
        ret.append(att.text)
    type_ = "tbody[id='prodForm:productContent:variants_data'] input[id*='type']"
    attributes = context.driver.find_elements(By.CSS_SELECTOR, type_)
    for att in attributes:
        ret.append(att.get_attribute("value"))
    return ret


@step('the attribute "(?P<att>.*)" wird angezeigt')
def step_impl(context, att):
    """
    :type context behave.runner.Context
    """
    has_attribute = False
    attributes = all_attributes(context)
    for attribute in attributes:
        if att in attribute:
            has_attribute = True
    assert has_attribute
    pass


@step("a drop down with the following entries is shown")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    items = allMenuItems(context, "energyClass")
    for label in context.table.rows:
        items.remove(label.cells[0])

    assert not items
