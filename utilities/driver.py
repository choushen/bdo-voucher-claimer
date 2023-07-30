import platform
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Check the user's operating system
if platform.system() == 'Windows':
    # Set path to Chrome WebDriver executable for Windows
    driver_path = 'path/to/chromedriver.exe'
elif platform.system() == 'Darwin' or platform.system().startswith('Mac'):
    # Set path to Chrome WebDriver executable for Mac
    driver_path = 'path/to/chromedriver'
else:
    # Set path to Chrome WebDriver executable for Linux
    driver_path = 'path/to/chromedriver'

# Initialize Chrome driver with executable path
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# Initialize Firefox driver with executable path
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--headless')
firefox_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)

# Check if Firefox is installed on the user's system
try:
    firefox_driver.get('about:blank')
except:
    firefox_installed = False
else:
    firefox_installed = True

# Use the appropriate driver based on the user's system and installed browsers
if firefox_installed:
    driver = firefox_driver
else:
    driver = chrome_driver

# Use driver to navigate to a website:
driver.get('https://www.example.com')

# Do something else...

# Close driver when finished
driver.quit()