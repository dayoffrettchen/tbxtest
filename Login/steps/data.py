from behave import *

from Login.TestMethods.selenium import writeById, press


use_step_matcher("re")



@When('type "(?P<text>.*)" in "(?P<id>\w*)"')
def step_impl(context, text, id):
    """
    :type context behave.runner.Context
    """
    writeById(context, id, text)
    pass


@When('press (?P<id>\w*)')
def step_impl(context,id):
    """
    :type context behave.runner.Context
    """
    press(context,id)
    pass