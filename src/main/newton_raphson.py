import logging
import main
import math


logger = logging.getLogger(__name__)


def calculate(function, function_prime, initial_value, *, tolerance=10**-5,
              max_iterations=25):

    logger.debug(f'0: {initial_value}')

    v0 = initial_value
    i = 1

    while True:

        if i > max_iterations:
            raise main.ConvergenceError(max_iterations)

        q = function(v0)
        p = function_prime(v0)

        if p == 0:
            raise main.ZeroDerivationError()

        v1 = v0 - q/p

        if math.fabs(v1-v0) < tolerance:
            logger.debug(f'{i}: {v1} - Answer')
            return v1

        logger.debug(f'{i}: {v1}')

        i += 1
        v0 = v1

    return None
