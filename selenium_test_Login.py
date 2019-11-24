import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

def testFailLogin():
    driver = webdriver.Safari()

    driver.maximize_window()
    driver.get('http://127.0.0.1:8000/admin/login/?next=/admin/')
    elem = driver.find_element_by_id("id_username")
    elem.send_keys("weixiang")
    elem = driver.find_element_by_id("id_password")
    elem.send_keys("09J48c96")
    elem.send_keys(Keys.RETURN)
    # driver.find_element_by_id("aBlog").click()
    
    assert "Log in | Django site admin" == driver.title
    driver.close()
    
def testPassLogin():
    driver = webdriver.Safari()

    driver.maximize_window()
    driver.get('http://127.0.0.1:8000/admin/login/?next=/admin/')
    elem = driver.find_element_by_id("id_username")
    elem.send_keys("WeiXiang")
    elem = driver.find_element_by_id("id_password")
    elem.send_keys("09J48c96")
    elem.send_keys(Keys.RETURN)
    # driver.find_element_by_id("aBlog").click()
    
    assert "Log in | Django site admin" == driver.title
    driver.close()
