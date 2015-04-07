from behave import *

from htx.Login.TestMethods.selenium import visit, visitNOWAIT
from htx.Login.environment import LOCALHOST_TBX_


use_step_matcher("re")

sites = {
    'onlineFFO': 'internal/onlineFulfillment.xhtml',
    'retailerEdit': 'slretailershop/retaileredit.xhtml',
    'productedit': 'product/productedit.xhtml',
    'login': 'login'
}


def addParameters(site, parameters):
    if parameters:
        site += "?"
    for param in parameters:
        site += param
        site += "="
        site += parameters[param]
        site += "&"
    return site
    pass


def visitSite(context, site, parameters={}, wait=True):
    site_ = sites[site]
    site_ = addParameters(site_, parameters)
    if wait:
        visit(context, site_)
    else:
        visitNOWAIT(context,site_)
    pass

@Given("open (?P<site>.*)")
def step_impl(context, site):
    """
    :type context behave.runner.Context
    :type context.driver webdriver
    """
    visitSite(context, site)


@Then("its shows log in Page")
def loginPage(context):
    context.driver.get(LOCALHOST_TBX_)
    assert "Eingelogged" in context.driver.page_source
    pass
