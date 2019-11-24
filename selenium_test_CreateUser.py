import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

def testFailedCreateUser():
    driver = webdriver.Safari()

    driver.maximize_window()
    driver.get('http://127.0.0.1:8000/admin/auth/user/add/')
    driver.find_element_by_id("id_username").send_keys("")
    driver.find_element_by_id("id_password1").send_keys("")
    driver.find_element_by_id("id_password2").send_keys("")
    # driver.find_element_by_id("aBlog").click()
    assert "" == driver.title
    driver.close()

def testPassedCreateUser():
    driver = webdriver.Safari()

    driver.maximize_window()
    driver.get('http://127.0.0.1:8000/admin/auth/user/add/')
    driver.find_element_by_id("id_username").send_keys("testuser")
    driver.find_element_by_id("id_password1").send_keys("password1")
    driver.find_element_by_id("id_password2").send_keys("password1")
    # driver.find_element_by_id("aBlog").click()
    assert "" == driver.title
    driver.close()
