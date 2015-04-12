from selenium import webdriver
from selenium.webdriver.common.by import By
from simplylocal.environment import config_map
from simplylocal.helper.htx.login import Login
from simplylocal.helper.htx.navigation import Navigation
from simplylocal.helper.htx.python.CheckBox import CheckBox


class Context:
    pass


driver = webdriver.Firefox()
config_map()
context = Context()
context.driver = driver
Login(context).log_in()
Navigation(context).visit_site("onlineFFO")
CheckBox("offo",context).select("Stuff","true")
CheckBox("offo",context).select("Stuff","false")

