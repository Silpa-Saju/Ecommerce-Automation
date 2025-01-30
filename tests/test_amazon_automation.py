import logging

import pytest
import allure

from conftest import driver
from pages.home_page import HomePage
from pages.product_page import ProductPage
from utils.logger import Logger

# Allure Report commands within a pytest class
@allure.feature('Automating Amazon shopping website')
@allure.story('Product search and validations')
class Test_Amazon:

    logger = Logger.get_logger(__name__)
    driver = None
    config = None
    # log_test_name = None

    @pytest.fixture(autouse=True)
    def setup(self, setup_driver, config):
        self.driver = setup_driver
        self.config = config
        # self.logger = logger_test_name


    def test_search_invalid_product(self):
        try:
            data = self.config.get("data",{}) # Get data section from config.ini
            # self.logger.info(f"Printing data ---> {data}")
            url = data["url"]
            invalidproductName = data["invalidproductname"]
            TestName = "Test to search for an invalid product on Amazon"
            self.logger.info(f"{TestName}")
            home = HomePage(self.driver)
            home.get_url(url)
            home.search_product(invalidproductName)
            home.retrieve_match_products_details(invalidproductName)
            home.check_matches_invalid_product(invalidproductName)
            self.logger.info(f"Test Passed :  {TestName}")
        except Exception as e:
            self.logger.error(f"Test Failed: Unable to search a product on Amazon due to : {e} ")


    # @allure.severity(allure.severity_level.NORMAL)
    # @allure.step("Perform search for a product on Amazon")
    def test_search_valid_product(self):
        try:
            data = self.config.get("data",{}) # Get data section from config.ini
            # self.logger.info(f"Printing data ---> {data}")
            url = data["url"]
            productName = data["productname"]
            TestName = "Test to search for a valid product on Amazon"
            self.logger.info(TestName)
            home = HomePage(self.driver)
            home.get_url(url)
            home.search_product(productName)
            home.retrieve_match_products_details(productName)
            home.check_matches_valid_product(productName)
            self.logger.info(f"Test Passed :  {TestName}")
        except Exception as e:
            self.logger.error(f"Test Failed: Unable to search a product on Amazon due to : {e} ")


    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.step("Saving extracted results from search page")
    def test_extract_and_save_search_results(self):
        try:
            data = self.config.get("data",{})  # Get data section from config.ini
            productName = data["productname"]
            filePath = data.get("filepath")
            writeoperation=data.get("writeoperation")
            TestName = "Test to extract  product results from on Amazon and save it to a csv file"
            self.logger.info(TestName)
            home = HomePage(self.driver)
            home.save_products_to_csv(filePath,writeoperation)
            self.logger.info(f"Test Passed :  {TestName}")
        except Exception as e:
            self.logger.error(f"Test Failed:  {e} ")

    def test_crawl_amazon_search_results(self):
        try:
            data = self.config.get("data", {})  # Get data section from config.ini
            crawlmaxpages = data["crawlmaxpages"]
            maxpages = int(crawlmaxpages)
            productName = data["productname"]
            filePath = data.get("filepath")
            appendoperation = data.get("appendoperation")
            TestName = "Test to crawl multiple pages of search results on Amazon and save it to a csv file"
            self.logger.info(TestName)
            page_count = 1
            home = HomePage(self.driver)
            while page_count <= maxpages:
                if not home.go_to_next_page():
                    break  # Stop if no next page
                self.logger.info(f"Navigating to page {page_count+1}  of search results")
                home.go_to_next_page()
                home.retrieve_match_products_details(productName)
                # home.check_matches_valid_product(productName)
                page_count += 1
            home.save_products_to_csv(filePath, appendoperation)
            self.logger.info(f"Test Passed :  {TestName}")
        except Exception as e:
            self.logger.error(f"Test Failed:  {e} ")

    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.step("Validate elements on Product page")
    def test_validate_elements_on_product_page(self):
        try:
            TestName = "Test to validate the Presence of elements 'AddToCart button', 'Product Descriptions', 'Image Gallery' on the product page"
            self.logger.info(TestName)
            home = HomePage(self.driver)
            product = ProductPage(self.driver)
            home.navigate_to_product_page()
            product.validate_presenceOf_addToCart_button_on_product_page()
            product.validate_presenceOf_product_desciption_on_product_page()
            product.validate_presenceOf_product_image_on_product_page()
            self.logger.info(f"Test Passed :  {TestName}")
        except Exception as e:
            self.logger.error(f"Test Failed : {e}")

