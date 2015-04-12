from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException

JS_JQUERY_DEFINED = "return typeof jQuery != 'undefined';"
JS_PRIMEFACES_DEFINED = "return typeof PrimeFaces != 'undefined';"
JS_JQUERY_ACTIVE = "return jQuery.active != 0;"
JS_PRIMEFACES_QUEUE_NOT_EMPTY = "return !PrimeFaces.ajax.Queue.isEmpty();"


def ajax_complete(driver):
    try:
        jquery = False
        primefaces = False
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


def visit_no_wait(context, site):
    context.driver.get(site)


def visit(context, site):
    context.driver.get(site)
    wait(context)


def press(context, button_id):
    button = context.driver.find_element_by_id(button_id)
    button.click()
    wait(context)


def select(ffo, label, check):
    if check == "true":
        if not ffo.is_selected():
            label.click()
    else:
        if ffo.is_selected():
            label.click()


def find_all_css(context, label):
    wait(context)
    labels = context.driver.find_elements(By.CSS_SELECTOR, label)
    return labels


def write_by_id(context, element_id, text):
    wait(context)
    input_element = context.driver.find_element_by_id(element_id)
    input_element.clear()
    input_element.send_keys(text)
    pass
