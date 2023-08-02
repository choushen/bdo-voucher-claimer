# Importing necessary modules and classes from selenium library
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# Importing Driver class from driver_utilities module
from driver_utilities.driver import Driver


# Xpath selectors for login and redeem code elements
img_login_logo_xpath = "//img[@alt='https://s1.pearlcdn.com/account/contents/img/common/logo_pearlabyss_id_v2.svg']"
header_redeem_code_xpath = "//h2[text()='Redeem Coupon Code']"

input_email_xpath = "//input[@id='_email']"
input_password_xpath = "//input[@id='_password']"
btn_login_xpath = "//button[@id='btnLogin']"

input_redeem_code_box1_xpath = "//input[@id='coupon01']"
input_redeem_code_box2_xpath = "//input[@id='coupon02']"
input_redeem_code_box3_xpath = "//input[@id='coupon03']"
input_redeem_code_box4_xpath = "//input[@id='coupon04']"
btn_redeem_code_xpath = "//a[@id='submitCoupon']"
alert_text_invalid = "This coupon code cannot be used multiple times."

# Function to perform login
def login(user_email: str, user_pwd: str):
    # Navigate to specific URL
    Driver._driver.get('https://payment.naeu.playblackdesert.com/en-US/Shop/Coupon')

    # Implicitly wait for a given amount of time (in seconds)
    Driver._driver.implicitly_wait(4) 

    # Find elements just before interacting with them
    input_email = Driver._driver.find_element(By.XPATH, input_email_xpath)
    input_password = Driver._driver.find_element(By.XPATH, input_password_xpath)
    btn_login = Driver._driver.find_element(By.XPATH, btn_login_xpath)

    # Checking if login logo is displayed
    if Driver._driver.find_element(By.XPATH, input_email_xpath).is_displayed():
        try:
            # Entering email and password into respective input fields, and then clicking on login button
            input_email.send_keys(user_email)
            input_password.send_keys(user_pwd)
            btn_login.click()
        except:
            # Exception handling for any other exceptions
            print("An error occurred while logging in. Exiting program.")
            Driver._driver.quit()
            raise SystemExit  # Exit the program with an error status

    else:
        # Initialize WebDriverWait instance with a timeout
        wait = WebDriverWait(Driver._driver, 20)

        try:
            # Wait until a certain condition is met, i.e., element becomes visible
            wait.until(EC.visibility_of_element_located((By.XPATH, header_redeem_code_xpath)))
        except TimeoutException:
            # Exception handling for TimeoutException
            print("Elements not found within the specified timeout. Exiting program.")
            Driver._driver.quit()  # Quit the driver if the condition isn't met within the timeout
            raise SystemExit  # Exit the program with an error status


# Function to input redeem codes
def input_codes(codes: list):

    # Initialize an empty dictionary to store results
    result = {}

    # Replace "-" in each code
    codes = [code.replace("-", "") for code in codes]

    # Iterate through list of codes
    for code in codes:

        # Find elements just before interacting with them
        input_redeem_code_box1 = Driver._driver.find_element(By.XPATH, input_redeem_code_box1_xpath)
        btn_redeem_code = Driver._driver.find_element(By.XPATH, btn_redeem_code_xpath)

        # Send code to input box and submit
        input_redeem_code_box1.send_keys(code)
        btn_redeem_code.click()

        # Implicitly wait for a given amount of time
        Driver._driver.implicitly_wait(2)

        # Switch to alert box
        alert = Driver._driver.switch_to.alert
        
        # Check alert text to determine success/failure
        if(alert_text_invalid == alert.text):
            # Store alert text and code in result dictionary
            result["result"] = alert.text
            result["code"] = code
            alert.accept()  # Accept the alert
            Driver._driver.switch_to.default_content()  # Switch back to default content
            reset_input_box()  # Clear input box
        else:
            # Store alert text and code in result dictionary
            result["result"] = alert.text
            result["code"] = code
            alert.accept()  # Accept the alert # Switch back to default content
            Driver._driver.implicitly_wait(2)
            Driver._driver.get('https://payment.naeu.playblackdesert.com/en-US/Shop/Coupon')
            Driver._driver.switch_to.default_content() 
    
    # Return the result dictionary
    return result


# Function to clear input boxes
def reset_input_box():
    # Find elements just before interacting with them
    input_redeem_code_box1 = Driver._driver.find_element(By.XPATH, input_redeem_code_box1_xpath)
    input_redeem_code_box2 = Driver._driver.find_element(By.XPATH, input_redeem_code_box2_xpath)
    input_redeem_code_box3 = Driver._driver.find_element(By.XPATH, input_redeem_code_box3_xpath)
    input_redeem_code_box4 = Driver._driver.find_element(By.XPATH, input_redeem_code_box4_xpath)

    # Clear each input box for the redeem code
    input_redeem_code_box1.clear()
    input_redeem_code_box2.clear()
    input_redeem_code_box3.clear()
    input_redeem_code_box4.clear()
