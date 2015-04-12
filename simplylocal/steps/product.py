from behave import *
from simplylocal.helper.htx.navigation import Navigation
from simplylocal.helper.htx.python.primefaces import all_menu_items

from simplylocal.helper.htx.sites.producttedit import ProductEdit


use_step_matcher("re")


def get_categories(category):
    return category.split('>')


@step('the category "(?P<category>.*)" is selected')
def step_impl(context, category=None):
    """
    :type context behave.runner.Context
    """
    Navigation(context).visit_site("productedit", {'id': 'new'})
    categories = get_categories(category)
    for cat in categories:
        ProductEdit(context).select_category(cat)


@step('the attribute "(?P<att>.*)" wird angezeigt')
def step_impl(context, att):
    has_attribute = False
    attributes = ProductEdit(context).all_attributes()
    for attribute in attributes:
        if att in attribute:
            has_attribute = True
    assert has_attribute


@step("a drop down with the following entries is shown")
def step_impl(context):
    attributes = ProductEdit(context).all_attributes()
    for attribute in attributes:
        print(attribute)
    items = all_menu_items(context, "energyClass")
    for label in context.table.rows:
        items.remove(label.cells[0])
    assert not items
