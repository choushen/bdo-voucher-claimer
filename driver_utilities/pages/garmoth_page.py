from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_utilities.driver import Driver


# Properties
url = 'https://garmoth.com/coupons'
xpath_coupon_id = "//section//h2[text()='Available']/..//input"


def get_codes():
    
    #Driver.instantiate_driver()
    # Use driver to navigate to a website:
    Driver._driver.get(url)

    # Get the codes
    wait = WebDriverWait(Driver._driver, 20)
    elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath_coupon_id)))
    codes = [element.get_attribute('id') for element in elements]
    
    return codes
