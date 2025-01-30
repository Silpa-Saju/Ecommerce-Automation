import csv
from contextlib import nullcontext

import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):

        def __init__(self,driver):
            super().__init__(driver)   # Inherits BasePage constructor to stor driver

        add_to_cart_button_elm = (By.ID, 'add-to-cart-button')
        product_description_elm = (By.ID, 'prodDetails')
        product_image_gallery_elm = (By.CSS_SELECTOR, '#landingImage')


        def validate_presenceOf_addToCart_button_on_product_page(self):
            try:
                self.logger.info("Validating presence of Add To Cart button on product page")
                if self.is_element_present(*self.add_to_cart_button_elm,20):
                    self.logger.info(f"PASS : 'Add To Cart' button is present on the product page")
            except Exception as e:
                self.logger.error(f"Unable to validate the presence of 'Add To Cart' button on the product page : {e}")

        def validate_presenceOf_product_desciption_on_product_page(self):
            try:
                self.logger.info("Validating presence of Product Description on product page")
                if self.is_element_present(*self.add_to_cart_button_elm):
                    self.logger.info(f"PASS : 'Product Description is present on the product page")
            except Exception as e:
                self.logger.error(f"Unable to validate the presence of 'Product Description' on the product page : {e}")

        def validate_presenceOf_product_image_on_product_page(self):
            try:
                self.logger.info("Validating presence of Product Image on product page")
                if self.is_element_present(*self.add_to_cart_button_elm):
                    self.logger.info(f"PASS : 'Product Image is present on the product page")
            except Exception as e:
                self.logger.error(f"Unable to validate the presence of 'Product Image' on the product page : {e}")

