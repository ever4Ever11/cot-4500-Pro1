import logging
import main
import math


logger = logging.getLogger(__name__)


def calculate(function, a, b, *, tolerance=10**-5, max_iterations=25):

    i = 0

    while True:

        if i > max_iterations:
            raise main.ConvergenceError(max_iterations)

        d = b - a
        c = b - d/2

        v = function(c)
        w = function(a)

        if math.fabs(d) < tolerance:
            logger.debug(f'{i}: {c} - Answer')
            return c

        logger.debug(f'{i}: {c}')

        # If increasing, where c is below the x-axis or
        # if decreasing, where c is above the x-axis
        if (w < 0 and v < 0) or (0 < w and 0 < v):
            a = c
        else:
            b = c

        i += 1

    return None
