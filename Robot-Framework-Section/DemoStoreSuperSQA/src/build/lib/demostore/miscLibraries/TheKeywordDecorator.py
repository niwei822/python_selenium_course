
from robot.api.deco import keyword
from robot.api import logger


@keyword("The user have requested a refund")
def user_requests_full_refund():
    logger.console("THE USER HAVE REQUESTED A REFUND")


def the_order_should_be_refunded_fully():
    logger.console("THE ORDER IS REFUNDED")