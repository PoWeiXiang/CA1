import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

def testFailedAccessBlog():
    driver = webdriver.Safari()

    driver.maximize_window()
    driver.get('http://127.0.0.1:8000/Blog/')
    # driver.find_element_by_id("aBlog").click()
    assert "" == driver.title
    driver.close()

def testPassedAccessBlog():
    driver = webdriver.Safari()

    driver.maximize_window()
    driver.get('http://127.0.0.1:8000/blog/')
    # driver.find_element_by_id("aBlog").click()
    assert "" == driver.title
    driver.close()
