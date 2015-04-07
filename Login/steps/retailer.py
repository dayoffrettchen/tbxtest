from behave import *

from Login.TestMethods.selenium import findAllCSS
from Login.steps.navigation import visitSite


use_step_matcher("re")


@then('ffo "(?P<ffo>.*)" is shown on retailerPage')
def step_impl(context, ffo):
    """
    :type context behave.runner.Context
    """
    visitSite(context, 'retailerEdit', parameters={'retailerid': 'campdavid'})
    all_label = findAllCSS(context, "#form\:offo>tbody>tr>td>label")
    for label in all_label:
        if ffo in label.text:
            return
    assert False
    pass