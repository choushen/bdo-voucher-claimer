from driver_utilities.pages.bdo_coupon_page import input_codes
from driver_utilities.pages.garmoth_page import get_codes
from driver_utilities.driver import Driver


codes:list = get_codes()

for code in codes:
    print(code)