from driver_utilities.driver import Driver
from driver_utilities.pages.garmoth_page import get_codes
from driver_utilities.pages.bdo_coupon_page import login, input_codes
#from gui import interface

Driver.instantiate_driver()

codes:list = get_codes()

# Testing code
for code in codes:
    print(code)

#login()
result = input_codes(codes)

#for code in result:
#    print(code)
#interface.start
