

from robot.api import logger



def example_of_args(p1, *args):

    logger.console('##################')
    logger.console("p1 is: {}".format(p1))
    logger.console("*args is: {}".format(args))
    logger.console("Type of args: {}".format(type(args)))
    for i in args:
        logger.console(i)
    logger.console('##################')


def example_of_kwargs(p1, **kwargs):

    logger.console('##################')
    logger.console("p1: {}".format(p1))
    logger.console("*kwargs is: {}".format(kwargs))
    logger.console("Type of kwargs: {}".format(type(kwargs)))
    for i in kwargs:
        logger.console(i)
    logger.console('##################')