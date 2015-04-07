from behave import *

use_step_matcher("re")

@Then("i should see (?P<text>.*)")
def step_impl(context, text):
    """
    :type context behave.runner.Context
    """
    assert text in context.driver.page_source
    pass

