from asyncio import wait_for
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from htx.Login.environment import LOCALHOST_TBX_


def ajax_complete(driver):
    try:
        return 0 == driver.execute_script("return jQuery.active")
    except WebDriverException:
        pass

def visit(context, site):
    context.driver.get(LOCALHOST_TBX_ + site)
    wait(context)


def press(context, buttonId):
    button = context.driver.find_element_by_id(buttonId)
    button.click()


def writeById(context, id, text):
    input = context.driver.find_element_by_id(id)
    input.send_keys(text)
    pass


def wait(context):
    WebDriverWait(context.driver, 10).until(
        ajax_complete, "Timeout waiting for page to load")


def my_automation_test():
    ff_driver = webdriver.Firefox()

    ff_driver.get("http://domain.tld")

    # wait for ajax items to load
    WebDriverWait(ff_driver, 10).until(
        ajax_complete, "Timeout waiting for page to load")

    assert "ajax loaded string" in ff_driver.page_source


def click_through_to_new_page(context, link_text):
    link = context.browser.find_element_by_link_text('my link')
    link.click()

    def link_has_gone_stale():
        try:
            # poll the link with an arbitrary call
            link.find_elements_by_id('doesnt-matter')
            return False
        except StaleElementReferenceException:
            return True

    wait_for(link_has_gone_stale)

