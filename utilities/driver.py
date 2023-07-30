import platform
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

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
ChromeDriverManager().install()
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_driver = webdriver.Chrome(options=chrome_options)

# Use driver to navigate to a website:
chrome_driver.get('https://www.example.com')

# Do something else...
time.sleep(5)
# Close driver when finished
chrome_driver.quit()