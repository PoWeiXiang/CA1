import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

def test():
    driver = webdriver.Safari()

    driver.maximize_window()
    driver.get('http://www.python.org')
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
