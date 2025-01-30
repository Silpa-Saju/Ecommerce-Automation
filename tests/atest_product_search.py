# import logging
#
# import pytest
#
# from pages.home_page import HomePage
#
#
# @pytest.mark.usefixtures("setup_driver") # This ensures the Webdriver setup is used before tests
# class Test_ProductSearch():
#
#     url = "https://www.amazon.in/"
#     productName = "Apple 2024 MacBook Air"
#     outputfilePath = 'product_info.csv'
#
#     def test_search_product(self,driver,url,productName):
#         try:
#             TestName = "Test to search for a product on Amazon"
#             logging.info(TestName)
#             home = HomePage(driver)
#             home.get_url(url)
#             home.search_product(productName)
#             logging.info(f"Test Passed :  {TestName}")
#         except Exception as e:
#             logging.error(f"Test Failed: Unable to search a product on Amazon due to : {e} ")
#
#
#     def test_extract_and_save_search_results(self,driver,productName,outputfilePath):
#         try:
#             TestName = "Test to extract  product results from on Amazon and save it to a csv file"
#             logging.info(TestName)
#             home = HomePage(driver)
#             home.retrieve_match_products_details(productName)
#             home.save_products_to_csv(outputfilePath)
#             logging.info(f"Test Passed :  {TestName}")
#         except Exception as e:
#             logging.error(f"Test Failed:  {e} ")
#
#
