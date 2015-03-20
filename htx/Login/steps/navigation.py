from behave import *
from htx.Login.TestMethods.selenium import visit
from htx.Login.environment import LOCALHOST_TBX_

use_step_matcher("re")

@Given("open (?P<site>.*)")
def step_impl(context, site):
    """
    :type context behave.runner.Context
    :type context.driver webdriver
    """
    visit(context, site)


@Then("its shows log in Page")
def loginPage(context):
    context.driver.get(LOCALHOST_TBX_)
    assert "Eingelogged" in context.driver.page_source
    pass
