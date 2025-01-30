# import logging
#
# import pytest
#
# from pages.product_page import ProductPage
#
#
# @pytest.mark.usefixtures("setup_driver") # This ensures the Webdriver setup is used before tests
# class Test_ProductPage():
#
#         def test_validate_elements_on_product_page(self,driver):
#             try:
#                 TestName = "Test to validate the Presence of elements 'AddToCart button', 'Product Descriptions', 'Image Gallery' on the product page"
#                 logging.info(TestName)
#                 product = ProductPage(driver)
#                 product.validate_presenceOf_addToCart_button_on_product_page()
#                 product.validate_presenceOf_product_desciption_on_product_page()
#                 product.validate_presenceOf_product_image_on_product_page()
#                 logging.info(f"Test Passed :  {TestName}")
#             except Exception as e:
#                 logging.error(f"Test Failed : {e}")