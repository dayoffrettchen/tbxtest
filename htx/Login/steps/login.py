from behave import *
from htx.Login.TestMethods.login import logIn, siteContains
from htx.Login.TestMethods.selenium import visit, press, visitNOWAIT

use_step_matcher("re")

@When("logged in")
def login(context):
    logIn(context)


@When("logged out")
def logedOut(context):
    pass


@Then("its shows welcome page")
def loginPage(context):
    visit(context, "")
    siteContains(context, "Willkommen")
    pass


def isLoggedIn(context):
    visit(context, "")
    return siteContains(context, "Eingeloggt als:")
    pass


def logOut(context):
    press(context, "name")
    pass


@given("logged in")
def step_impl(context):
    """
    :type context behave.runner.Context
    :type context.driver webdriver
    """
    if isLoggedIn(context):
        logOut(context)
    logIn(context)
    pass


@given("as '(?P<login>.*)' logged in")
def step_impl(context, login):
    """
    :type context behave.runner.Context
    """
    if isLoggedIn(context):
        logOut(context)
    logIn(context, login)


@then("it should be illegal to call (?P<site>.*)")
def step_impl(context, site):
    """
    :type context behave.runner.Context
    """
    visitNOWAIT(context,site)
    assert "403" in context.driver.page_source
    pass