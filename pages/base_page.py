from logging import exception

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.logger import Logger
import time


class BasePage:

    def __init__(self,driver):
        self.driver=driver

    # Use the Logger to get an instance of logger
    logger = Logger.get_logger()

    def get_url(self,url):
        try:
            self.logger.info(f"Navigating to URL :  {url}")
            self.driver.get(url)
            # self.logger.info(f"Navigating to URL :  {url}")
            # self.driver.maximize_window()
        except Exception as e:
            self.logger.error(f"Error opening the URL {url} : {e}")
            raise  # re-raises the caught exception & allow the function to terminate the prgm


    def find_element(self,by,locator,timeout=10):
        try:
            element = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((by,locator)))
            # Highlighting the element using Javascript
            self.driver.execute_script("arguments[0].style.border='3px solid red'",element)
            return element
        except Exception as e :
            self.logger.error(f"Error finding the element {locator} by {by} :  {e}")
            raise


    def find_elements(self,by,locator,timeout=10):
        try:
            elements = WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located((by,locator)))
            return elements
        except Exception as e :
            self.logger.error(f"Error finding the element {locator} by {by} :  {e}")
            raise

    def len_find_elements(self, by, locator, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((by, locator))  # Wait for all elements
            )
            return len(elements)  # Return the count of elements
        except Exception as e:
            self.logger.error(f"Error finding elements {locator} by {by}: {e}")
            return 0  # Return 0 instead of raising an exception (optional)

    def click(self,by,locator):
        try:
            element = self.find_element(by,locator)
            element.click()
            time.sleep(20)
        except Exception as e:
            self.logger.error(f"Error clicking the element {locator} by {by} : {e}")
            raise

    def enter_text(self,by,locator,text, press_enter =False):
        try:
            element = self.find_element(by,locator)
            element.clear()
            element.send_keys(text)
            if press_enter:
                element.send_keys(Keys.RETURN)
        except Exception as e:
            self.logger.error(f"Error entering text {text} into the element {locator} by {by} : {e}")
            raise


    def is_element_present(self,by,locator,timeout=10):
        try:
            element = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((by,locator)))
            # Highlighting the element using Javascript
            self.driver.execute_script("arguments[0].style.border='3px solid red'",element)
            # Check if element is present or not
            return element.is_displayed() and element.is_enabled()
        except Exception as e :
            self.logger.warning(f"Element {locator} by {by} not found or visible:  {e}")
            return False

    def is_element_displayed(self,by,locator,timeout=10):
        try:
            element = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((by,locator)))
            # Highlighting the element using Javascript
            self.driver.execute_script("arguments[0].style.border='3px solid red'",element)
            # Check if element is present or not
            return element.is_displayed()
        except Exception as e :
            self.logger.warning(f"Element {locator} by {by} not visible:  {e}")
            return False

    def get_text_of_subelement_with_default(self,base, by, locator, default="NA"):
        try:
            return base.find_element(by, locator).text.strip()
        except Exception:
            return default

    def get_attribute_of_subelement_with_default(self, base, by, locator, attribute, default="NA"):
        try:
            return base.find_element(by, locator).get_attribute(attribute)
        except Exception:
            return default


