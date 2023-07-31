import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Driver:
    _driver = None
    
    @classmethod
    def instantiate_driver(cls):
        if cls._driver is None:
            cls._driver = cls._create_driver()
            
    @classmethod
    def _create_driver(cls):
        # Initialize Chrome driver with executable path
        ChromeDriverManager().install()
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        return driver
        
    @classmethod
    def kill_driver(cls):
        # Close driver when finished
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
        
    