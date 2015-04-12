from behave import *
from simplylocal.helper.htx.navigation import Navigation
from simplylocal.helper.htx.sites.onlineFFO import OnlineFFO

from simplylocal.helper.selenium import *
from simplylocal.helper.selenium.selenium import press


use_step_matcher("re")


@when('add "(?P<ffo>.*)" to onlineFulfillment')
def step_impl(context, ffo):
    OnlineFFO(context).add_ffo(ffo)


@then('there should be no "(?P<text>.*)"')
def step_impl(context, text):
    assert not OnlineFFO(context).has_ffo(text)


@then("there should be (?P<text>.*)")
def step_impl(context, text):
    assert OnlineFFO(context).has_ffo(text)


@step('remove "(?P<ffo>.*)" from onlineFulfillment')
def step_impl(context, ffo):
    OnlineFFO(context).remove_ffo(ffo)


@step('there should one "(?P<text>.*)"')
def step_impl(context, text):
    assert OnlineFFO(context).count_ffo(text) == 1


@step('"(?P<text>.*)" is added to onlineFulfillment')
def step_impl(context, text):
    OnlineFFO(context).add_ffo(text)


@step('the onlineFFO "(?P<ffo>.*)" is "(?P<checked>.*)"')
def step_impl(context, ffo, checked):
    if OnlineFFO(context).is_checked(ffo):
        assert checked == "true"
    else:
        assert checked == "false"

@when('the onlineFFO "(?P<ffo>.*)" set "(?P<checked>.*)"')
def step_impl(context, ffo, checked):
    OnlineFFO(context).select_ffo(ffo, checked)

@when("save the onlineFFO")
def step_impl(context):
    OnlineFFO(context).save()

@when("all onlineFFO are deleted")
def step_impl(context):
    online_ffo = OnlineFFO(context)
    online_ffo.online_ffo_menu_item()
    all_text = [y.text for y in online_ffo.online_ffo_menu_item()]
    for ffo in all_text:
        online_ffo.remove_ffo(ffo)


@then("no onlineFFO are shown")
def step_impl(context):
    assert not OnlineFFO(context).online_ffo_menu_item()


@then('ffo "(?P<ffo>.*)" is shown on retailerPage')
def step_impl(context, ffo):
    Navigation(context).visit_site('retailerEdit', parameter={'retailerid': 'campdavid'})
    for label in OnlineFFO(context).online_ffo_menu_item():
        if ffo in label.text:
            return
    assert False

