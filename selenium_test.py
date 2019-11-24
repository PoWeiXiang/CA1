import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

def testFailedAccessProjects():
    driver = webdriver.Safari()

    driver.maximize_window()
    driver.get('http://127.0.0.1:8000/Projects/')
    # driver.find_element_by_id("aBlog").click()
    assert "" == driver.title
    driver.close()

def testPassedAccessProjects():
    driver = webdriver.Safari()

    driver.maximize_window()
    driver.get('http://127.0.0.1:8000/projects/')
    # driver.find_element_by_id("aBlog").click()
    assert "" == driver.title
    driver.close()



