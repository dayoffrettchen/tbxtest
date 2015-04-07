from asyncio import wait_for

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException

from Login.environment import LOCALHOST_TBX_
JS_JQUERY_DEFINED = "return typeof jQuery != 'undefined';";
JS_PRIMEFACES_DEFINED = "return typeof PrimeFaces != 'undefined';";
JS_JQUERY_ACTIVE = "return jQuery.active != 0;";
JS_PRIMEFACES_QUEUE_NOT_EMPTY = "return !PrimeFaces.ajax.Queue.isEmpty();";

def ajax_complete(driver):
    try:
        if driver.execute_script(JS_JQUERY_DEFINED):
            jquery = driver.execute_script(JS_JQUERY_ACTIVE)
        if driver.execute_script(JS_PRIMEFACES_DEFINED):
            primefaces = driver.execute_script(JS_PRIMEFACES_QUEUE_NOT_EMPTY)
        return not jquery or primefaces
    except WebDriverException:
        pass

def wait(context):
    WebDriverWait(context.driver, 10, poll_frequency=200).until(
        ajax_complete, "Timeout waiting for page to load")


def visitNOWAIT(context, site):
    context.driver.get(LOCALHOST_TBX_ + site)


def visit(context, site):
    context.driver.get(LOCALHOST_TBX_ + site)
    wait(context)


def press(context, buttonId):
    button = context.driver.find_element_by_id(buttonId)
    button.click()
    wait(context)


def select(context, ffo, check):
    if check:
        if not ffo.is_selected():
            ffo.click()
    else:
        if ffo.is_selected():
            ffo.click()


def findAllCSS(context, label):
    wait(context)
    labels = context.driver.find_elements(By.CSS_SELECTOR, label)
    return labels


def writeById(context, id, text):
    wait(context)
    input = context.driver.find_element_by_id(id)
    input.clear()
    input.send_keys(text)
    pass

def allMenuItems(contex, id=""):
    wait(contex)
    elements = contex.driver.find_elements(By.CSS_SELECTOR, "div[id$='" + id + "_panel']")
    if len(elements) > 1:
        return
    ret = []
    items = selectManyMenuItems(elements[0])

    for item in items:
        ret.append(item.get_attribute("innerHTML"))
    return ret


def selectManyMenuItems(menu):
    return menu.find_elements(By.CSS_SELECTOR, "li")


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

