# Webdriver Setup
import logging
import os.path

import pytest
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utils.logger import Logger

# Use the Logger to get an instance of logger
logger = Logger.get_logger()

# Global variable to store the WebDriver instance
driver = None

#Defining the fixture to return the driver
@pytest.fixture(scope="session",params=["chrome"])
def setup_driver(request):
    # # Ensure the fixture is called only once per class
    # if not hasattr(request.cls, "driver"):
    global driver
    if driver is None:
        if request.param=="chrome":
            service = ChromeService(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass detection
            # Initialize the WebDriver
            driver = webdriver.Chrome(service=service, options=options)

        elif request.param=="edge":
            service = EdgeService(EdgeChromiumDriverManager().install())
            options = webdriver.EdgeOptions()
            options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass detection
            # Initialize the WebDriver
            driver = webdriver.Edge(service=service, options=options)

        elif request.param == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass detection
            # Initialize the WebDriver
            driver = webdriver.Firefox(service=service, options=options)

        driver.maximize_window()
        # request.cls.driver=driver
    yield driver

    # Quit the driver after all tests are done
    request.addfinalizer(driver.quit)
    # # After the test class is finished, quit the driver
    # if hasattr(request.cls, "driver"):
    #     driver.quit()

@pytest.fixture(scope="session",params=["chrome","edge"])
def setup_grid_driver(request):
    # # Ensure the fixture is called only once per class
    # if not hasattr(request.cls, "driver"):
    remote_url="http://localhost:4444/wd/hub"
    global driver
    if driver is None:
        if request.param=="chrome":
            options = webdriver.ChromeOptions()
            # driver = webdriver.Chrome(ChromeDriverManager().install())

        elif request.param=="edge":
            options = webdriver.EdgeOptions()

        elif request.param == "firefox":
            options = webdriver.FirefoxOptions()

        options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass detection
        driver = webdriver.Remote(command_executor=remote_url,options=options)
        driver.maximize_window()
        # request.cls.driver=driver
    yield driver

    # Quit the driver after all tests are done
    request.addfinalizer(driver.quit)
    # # After the test class is finished, quit the driver
    # if hasattr(request.cls, "driver"):
    #     driver.quit()


#Defining the fixture to load values from config.ini file
@pytest.fixture(scope="session")
def config():

    try:
        config = configparser.ConfigParser()

        #Get the root directory of project
        project_root = os.path.abspath(os.path.dirname(__file__)) # Gets directory of current script (conftest.py)
        # Checking if config file exists
        config_path = os.path.join(project_root,"config.ini")
        if not os.path.exists(config_path):
            logger.error(f"Config file not found at file path :  {config_path} ")
            raise FileNotFoundError(f"Config file not found at file path :  {config_path} ")

        config.read(config_path)
        #Debugging : available log sections
        sections = config.sections()
        logger.info(f"Loaded config file :  {config_path}")
        # logger.info(f"Available sections in config file : {sections}")

        if not sections:
            logger.error(f"No sections found in file : {config_path}")
            raise ValueError(f"No sections found in file : {config_path}")

        #Convert sections into dictionary
        config_dict = {section: dict(config.items(section)) for section in sections}
        # print(f"Config dict ---> {config_dict}")
        return config_dict   #Return all sections as a dictionary

    except Exception as  e:
        logger.error(f"Error reading config file :  {e}")
        raise





