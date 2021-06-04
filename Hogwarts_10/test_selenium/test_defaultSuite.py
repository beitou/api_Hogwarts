# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestDefaultSuite():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_search(self):
    self.driver.get("https://testerhome.com/")
    self.driver.set_window_size(1393, 877)
    self.driver.find_element(By.NAME, "q").click()
    self.driver.find_element(By.NAME, "q").send_keys("霍格沃兹测试学院")
    self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    time.sleep(3)
    self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院").click()
    assert "霍格沃兹测试学院" in self.driver.page_source


  