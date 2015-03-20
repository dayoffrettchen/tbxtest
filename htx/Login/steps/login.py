from behave import *
from htx.Login.TestMethods.login import logIn, siteContains
from htx.Login.TestMethods.selenium import visit


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


@given("logged in")
def step_impl(context):
    """
    :type context behave.runner.Context
    :type context.driver webdriver
    """

    if not isLoggedIn(context):
        login(context)
    pass