

from demostore.demostoreConfigs.couponConfigs import COUPONS
import random
from robot.api import logger
from robot.api.deco import keyword



class Coupons(object):



    @keyword("Get a valid coupon")
    def get_valid_coupon(self):
        """

        Returns:

        """
        logger.console("Getting valid coupon")
        return random.choice(COUPONS['valid'])

    @keyword("Get an expired coupon")
    def get_expired_coupon(self):
        """

        Returns:

        """

        logger.console("Getting valid coupon")
        return random.choice(COUPONS['expired'])


    @keyword("Discount should be calculated correctly")
    def discount_should_be_calculated_correctly(self, original_price, discounted_price, discount_percentage):
        """
        Given the original price and discounted price, this method verifies the given percentage is applied correctly
        to the original price to get the discounted price.
        :param original_price:
        :param discounted_price:
        :param discount_percentage:
        :return:
        """

        original_price = original_price.replace('$', '')
        original_price = float(original_price)

        discounted_price = discounted_price.replace('$', '')
        discounted_price = float(discounted_price)


        discount = original_price * (discount_percentage / 100)
        expected_discounted = original_price - discount + 1

        if expected_discounted != discounted_price:
            raise Exception("The discounted price is not correct. Discount percentage: {percentage}%, "
                            "Original price: ${original}, Expected discounted: ${exp}, Actual discounted: ${act}"
                            .format(percentage=discount_percentage,
                                    original=original_price,
                                    exp=expected_discounted,
                                    act=discounted_price))
        else:
            logger.console("Discount calculated correctly.")