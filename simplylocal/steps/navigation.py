from behave import *
from simplylocal.environment import config_map
from simplylocal.helper.htx.navigation import Navigation


use_step_matcher("re")


@Given("open (?P<site>.*)")
def step_impl(context, site):
    Navigation(context).visit_site(site)


@Then("its shows log in Page")
def step_impl(context):
    context.driver.get(config_map()['url'])
    assert "Eingelogged" in context.driver.page_source
