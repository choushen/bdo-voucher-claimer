from selenium import webdriver
import platform

# Set path to Firefox WebDriver executable

if platform.system() == 'Windows':
    driver_path = 'utilities/geckodriver-windows.exe'
elif platform.system() == 'MacOS':
    driver_path = 'utilities/geckodriver-mac'



# Set options for Firefox browser
firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True

# Initialize Firefox driver with options and executable path
driver = webdriver.Firefox(executable_path=driver_path, options=firefox_options)

# Use driver to navigate to a website:
driver.get('https://www.example.com')

# Do something else...

# Close driver when finished
driver.quit()