import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

def testFailedCreatePost():
    driver = webdriver.Safari()

    driver.maximize_window()
    driver.get('http://127.0.0.1:8000/admin/blog/post/add/')
    driver.find_element_by_id("id_title").send_keys("")
    driver.find_element_by_id("id_body").send_keys("")
    driver.find_element_by_xpath("//select/option[@value='5']").click()
    driver.find_element_by_xpath("//submit[@type='submit' and @value='Save']").click()    
    # driver.find_element_by_id("aBlog").click()
    assert "" == driver.title
    driver.close()

def testPassedCreatePost():
    driver = webdriver.Safari()

    driver.maximize_window()
    driver.get('http://127.0.0.1:8000/admin/blog/post/add/')
    driver.find_element_by_id("id_title").send_keys("Listening Music")
    driver.find_element_by_id("id_body").send_keys("HipHop music, Rap music")
    driver.find_element_by_xpath("//select/option[@value='5']").click()
    driver.find_element_by_xpath("//submit[@type='submit' and @value='Save']").click()    
    # driver.find_element_by_id("aBlog").click()
    assert "" == driver.title
    driver.close()
