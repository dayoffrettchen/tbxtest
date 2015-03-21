from behave import *
from htx.Login.TestMethods.selenium import *

use_step_matcher("re")


def addFFO(context, ffo):
    wait(context)
    writeById(context, "addOffo", ffo)
    press(context, "add")
    wait(context)


@when('add "(?P<ffo>.*)" to onlineFulfillment')
def step_impl(context, ffo):
    """
    :type context behave.runner.Context
    """
    addFFO(context, ffo)


@then('there should be no "(?P<text>.*)"')
def step_impl(context, text):
    """
    :type context behave.runner.Context
    """
    assert not hasFFO(context, text)


@then("there should be (?P<text>.*)")
def step_impl(context, text):
    """
    :type context behave.runner.Context
    """
    assert hasFFO(context, text)


def countFFO(context, ffo):
    count = 0
    wait(context)
    all_css = findAllCSS(context, "#offo>tbody>tr>td>label")
    for label in all_css:
        if label.text == ffo:
            count += 1
    return count


def isChecked(context, ffo):
    wait(context)
    all_css = findAllCSS(context, "#offo>tbody>tr>td>label")
    for label in all_css:
        if label.text == ffo:
            return context.driver.find_element_by_id(label.get_attribute("for")).is_selected()

def hasFFO(context, ffo):
    wait(context)
    all_css = findAllCSS(context, "#offo>tbody>tr>td>label")
    for label in all_css:
        if label.text == ffo:
            return True

def findFFO(context, ffo):
    wait(context)
    all_css = findAllCSS(context, "#offo>tbody>tr>td>label")
    for label in all_css:
        if label.text == ffo:
            return label

def removeFFO(context, ffo):
    writeById(context, "addOffo", ffo)
    press(context, "remove")


@step('remove "(?P<ffo>.*)" from onlineFulfillment')
def step_impl(context, ffo):
    """
    :type context behave.runner.Context
    """
    removeFFO(context, ffo)


@step('there should one "(?P<text>.*)"')
def step_impl(context, text):
    """
    :type context behave.runner.Context
    """

    assert countFFO(context, text) == 1


@step('"(?P<text>.*)" is added to onlineFulfillment')
def step_impl(context,text):
    """
    :type context behave.runner.Context
    """
    addFFO(context,text)
    pass


@step('the onlineFFO "(?P<ffo>.*)" is "(?P<checked>.*)"')
def step_impl(context,ffo,checked):
    """
    :type context behave.runner.Context
    """
    if isChecked(context, ffo):
        assert checked == "true"
    else:
        assert checked == "false"
    pass


@when('the onlineFFO "(?P<ffo>.*)" set "(?P<checked>.*)"')
def step_impl(context, ffo, checked):
    """
    :type context behave.runner.Context
    """
    select(context,findFFO(context, ffo),checked=='true')
    pass


@when("save the onlineFFO")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    press(context, "save")
    pass