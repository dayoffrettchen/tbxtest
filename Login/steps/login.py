from behave import *

from Login.TestMethods.login import logIn, siteContains
from Login.TestMethods.selenium import visit, press
from Login.steps.navigation import visitSite


use_step_matcher("re")

@When("logged in")
def login(context):
    logIn(context)


@When("logged out")
def logedOut(context):
    logOut(context)
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
    if isLoggedIn(context):
        logOut(context)
    logIn(context, login)


@then("it should be illegal to call (?P<site>.*)")
def step_impl(context, site):
    """
    :type context behave.runner.Context
    """
    visitSite(context, site, wait=False)
    assert "403" in context.driver.page_source
    pass
