from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_utilities.driver import Driver

def input_codes(user_email: str, user_pwd: str, codes: list):
    # Use driver to navigate to a website:
    Driver._driver.get('https://payment.naeu.playblackdesert.com/en-US/Shop/Coupon')
    
    input_email = Driver._driver.find_element_by_xpath("//input[@id='_email']")
    input_password = Driver._driver.find_element_by_xpath("//input[@id='_password']")
    btn_login = Driver._driver.find_element_by_xpath("//button[@id='btnLogin']")
    
    if input_email.is_displayed():
        input_email.send_keys(user_email)
        input_password.send_keys(user_pwd)
        btn_login.click()
    else:
        print('Already logged in')