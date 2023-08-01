from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from driver_utilities.driver import Driver

# Login elements
img_login_logo = "//img[@alt='https://s1.pearlcdn.com/account/contents/img/common/logo_pearlabyss_id_v2.svg']"
input_email = Driver._driver.find_element_by_xpath("//input[@id='_email']")
input_password = Driver._driver.find_element_by_xpath("//input[@id='_password']")
btn_login = Driver._driver.find_element_by_xpath("//button[@id='btnLogin']")

# Redeem code elements
header_redeem_code_header = Driver._driver.find_element_by_xpath("//h2[text()='Redeem Coupon Code']")
input_redeem_code_box1 = Driver._driver.find_element_by_xpath("//input[@id='_couponCode1']")
input_redeem_code_box2 = Driver._driver.find_element_by_xpath("//input[@id='_couponCode2']")
input_redeem_code_box3 = Driver._driver.find_element_by_xpath("//input[@id='_couponCode3']")
input_redeem_code_box4 = Driver._driver.find_element_by_xpath("//input[@id='_couponCode4']")
btn_redeem_code = Driver._driver.find_element_by_xpath("//a[@id='submitCoupon']")


def login(user_email: str, user_pwd: str):
        # Use driver to navigate to a website:
    Driver._driver.get('https://payment.naeu.playblackdesert.com/en-US/Shop/Coupon')
    
    # Set the implicit wait time (in seconds)
    Driver._driver.implicitly_wait(2) 

    if img_login_logo.is_displayed():
        input_email.send_keys(user_email)
        input_password.send_keys(user_pwd)
        btn_login.click()
    else:
        wait = WebDriverWait(Driver._driver, 20)
        try:
            wait.until(EC._element_if_visible(header_redeem_code_header))
        except TimeoutException:
            print("Elements not found within the specified timeout. Exiting program.")
            Driver._driver.quit()  # Quit the driver
            raise SystemExit  # Exit the program with an error status


def input_codes(codes: list):
    
    result = {}

    for code in codes:

        input_redeem_code_box1.send_keys(code)
        input_redeem_code_box1.submit()

        list.pop(code)

        Driver._driver.implicitly_wait(2)

        alert = Driver._driver.switch_to.alert
        
        if(alert and alert.text == "Invalid coupon code."):
            result["result"] = alert.text
            result["code"] = code
            alert.accept()

        reset_input_box()


def reset_input_box():
    input_redeem_code_box1.clear()
    input_redeem_code_box2.clear()
    input_redeem_code_box3.clear()
    input_redeem_code_box4.clear()