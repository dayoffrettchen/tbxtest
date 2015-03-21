from behave import *
from htx.Login.TestMethods.selenium import findAllCSS

use_step_matcher("re")

@Then("i should see (?P<text>.*)")
def step_impl(context, text):
    """
    :type context behave.runner.Context
    """
    assert text in context.driver.page_source
    pass

