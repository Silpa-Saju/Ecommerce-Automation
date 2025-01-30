import csv
import time
from operator import truediv

import pytest
import os

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pathlib import Path


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)  # Inherits BasePage constructor to store driver
        self.match_products = []


    amazonSearch_box = (By.ID, 'twotabsearchtextbox') #tuple
    search_results = (By.XPATH, "//span[contains(text(),'results')]")
    results_elements = (By.CSS_SELECTOR, "div.s-search-results div[role='listitem']")
    product_name_elm = (By.CSS_SELECTOR, 'h2 span')
    product_ratings_elm = (By.CSS_SELECTOR, 'i.a-icon.a-icon-star-small span')
    product_price_elm = (By.CSS_SELECTOR, 'span.a-price-whole')
    product_url_elm = (By.CSS_SELECTOR, 'a.a-link-normal')
    next_page_locator = (By.CSS_SELECTOR,'a.s-pagination-next')



    def search_product(self,productName):
        try:
            self.logger.info(f"Searching for product {productName} in Home page")
            self.enter_text(*self.amazonSearch_box,productName,True)
            self.logger.info(f"Checking if results are loaded for the product search")
            if self.is_element_present(*self.search_results):
                self.logger.info(f"PASS : Results got loaded for product {productName}")
            else:
                assert self.is_element_present(), f"No results are loaded found for product {productName}"
        except Exception as e:
            self.logger.error(f"Error searching for product {productName} : {e}")
            raise


    def retrieve_match_products_details(self,productName):
        try:
            self.products_list = self.find_elements(*self.results_elements)
            self.len_products = self.len_find_elements(*self.results_elements)
            self.logger.info(f"Total count of products list after search : {self.len_products}")

            # Looping through all products elements that matches the search value
            self.logger.info(f"Looping through all products elements that matches the search value")
            for product in self.products_list:
                product_name = self.get_text_of_subelement_with_default(product,*self.product_name_elm)

                if productName.lower() in product_name.lower():
                    product_ratings = self.get_text_of_subelement_with_default(product, *self.product_ratings_elm)
                    product_pricing =  self.get_text_of_subelement_with_default(product, *self.product_price_elm)
                    product_url = self.get_attribute_of_subelement_with_default(product, *self.product_url_elm,"href")
                    self.match_products.append([product_name,product_pricing,product_ratings,product_url])
                #  Search stops until 5 matching products are got
                if len(self.match_products)==5:
                    break
        except Exception as e:
                self.logger.error(f" ERROR :   {e}")
                raise

    def check_matches_valid_product(self,productName):
        try:
            self.logger.info(f"Checking if any matching products are found")
            if self.match_products:
                self.logger.info(f"PASS: Found matching products for product {productName}")
            else:
                self.logger.error(f"ERROR : no matching products found for product {productName} from search results")
                assert False, f"No matching products found for product {productName} from search results"
        except Exception as e:
            self.logger.error(f" ERROR :   {e}")
            raise

    def check_matches_invalid_product(self,productName):
        try:
            self.logger.info(f"Checking if any matching products are found")
            if self.match_products:
                self.logger.error(f"Error: Found matching products for invalid product {productName}")
                assert False, f"Found matching products for invalid product {productName}"
            else:
                self.logger.info(f"PASS : no matching products found for product {productName} from search results")
        except Exception as e:
            self.logger.error(f" ERROR :   {e}")
            raise

    def save_products_to_csv(self,filePath,fileoperation):
        try:

            self.logger.info(f"Saving the extracted product information in a CSV file {filePath}")
            # Get the root directory of the project using Pathlib
            project_root = Path(__file__).resolve().parents[1]  # Get 1 levels from the current file
            # self.logger.info(f"Project_root --> {project_root}")
            # Define the log file path relative to the root directory (outputs folder)
            log_dir = os.path.join(project_root, "outputs")
            # self.logger.info(f"log_dir --> {log_dir}")

            # Ensure the outputs directory exists
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)  # Create the folder if it doesn't exist

            # Full path to the log file
            outputfilePath = os.path.join(log_dir, filePath)
            # self.logger.info(f"outputfilePath --> {outputfilePath}")

            with open(outputfilePath,f"{fileoperation}",newline='',encoding='utf-8') as file:
                writer = csv.writer(file)
                if fileoperation=='w':
                  writer.writerow(['Product_Name','Product_Price','Product_Ratings','Product_URL'])
                writer.writerows(self.match_products)
                self.logger.info("PASS: successfully saved the product information to a csv file")
        except Exception as e:
               self.logger.error(f"ERROR : Product information can't be saved to a csv file : {e}")


    def navigate_to_product_page(self):
        try:
            self.products_list = self.find_elements(*self.results_elements)
            # Extracting 1 product (1st)
            self.logger.info(f"Retrieving the url for 1st product that matches the search value ")
            for i, product in enumerate(self.products_list[:5]):
                self.product_name = self.get_text_of_subelement_with_default(product,*self.product_name_elm)
                self.product_url = self.get_attribute_of_subelement_with_default(product, *self.product_url_elm, "href")
                if self.product_url is not None:
                    self.logger.info(f"Navigating to the 1st match product page")
                    self.get_url(self.product_url)
                    return
        except Exception as e:
            self.logger.error(f"ERROR : Unable to navigate to url of product {self.product_name} : {e}")



    def go_to_next_page(self):
        """Navigates to next page if avaiable"""
        try:
            self.logger.info(f"Checking navigation to next page is available")
            if self.is_element_present(*self.next_page_locator,20):
                self.logger.info(f"Clicking paginator for navigation to next page")
                self.click(*self.next_page_locator)
                return True
            else:
                self.logger.info(f"Navigation to next page is not avaiable")
                return False
        except Exception as e:
                self.logger(f"Unable to navigate next page :  {e}")
                return False






        except Exception as e:
            self.logger.error(f"")