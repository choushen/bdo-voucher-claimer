from driver_utilities.pages.bdo_coupon_page import input_codes
from driver_utilities.pages.garmoth_page import get_codes
from driver_utilities.driver import Driver
from gui import interface



codes:list = get_codes()

# Testing code
for code in codes:
    print(code)


result = input_codes(codes)

for code in result:
    print(code)
#interface.start
