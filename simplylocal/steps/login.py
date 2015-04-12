from behave import *

from simplylocal.helper.htx.login import Login
from simplylocal.helper.htx.navigation import Navigation
from simplylocal.helper.selenium.selenium import write_by_id, press


use_step_matcher("re")


@When('type "(?P<text>.*)" in "(?P<id>\w*)"')
def step_impl(context, text, element_id):
    write_by_id(context, element_id, text)
    pass


@When('press (?P<id>\w*)')
def step_impl(context, element_id):
    press(context, element_id)
    pass


@Then('i should see (?P<text>.*)')
def step_impl(context, text):
    assert text in context.driver.page_source
    pass


@When("logged in")
def step_impl(context):
    Login(context).log_in()


@When("logged out")
def step_impl(context):
    Login(context).log_out()


@Then("its shows welcome page")
def step_impl(context):
    Navigation(context).visit_site("welcome")
    assert "Welcome" in context.driver.page_source


@given("logged in")
def step_impl(context):
    Login(context).log_in()


@given("as '(?P<login>.*)' logged in")
def step_impl(context, login):
    Login(context).log_in(login)


@then("it should be illegal to call (?P<site>.*)")
def step_impl(context, site):
    Navigation(context).visit_site(site, wait=False)
    assert "403" in context.driver.page_source
