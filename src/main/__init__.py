import sympy.core.function
import sympy.core.symbol
import sympy.parsing.sympy_parser
import sympy.utilities.lambdify


class ConvergenceError(Exception):
    """Raised when max iterations exceeded"""

    def __init__(self, max_iterations):
        self.message = f'failed to converge in {max_iterations} iterations'
        return None

    def __str__(self):
        return self.message


class ZeroDerivativeError():
    """Raised when a derivative of zero is calculated"""

    def __str__(self):
        return 'detected zero derivative'


def strtofun0(function):
    x = sympy.core.symbol.symbols('x')
    function = sympy.parsing.sympy_parser.parse_expr(function)
    return sympy.utilities.lambdify(x, function)


def strtofun1(function):
    x = sympy.core.symbol.symbols('x')
    function = sympy.parsing.sympy_parser.parse_expr(function)
    function_prime = sympy.core.function.diff(function, x)
    return sympy.utilities.lambdify(x, function_prime)
