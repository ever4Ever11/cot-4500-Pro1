import main
import main.bisection
import unittest


class Test_Bisection(unittest.TestCase):

    def test_calculate(self):

        function = main.strtofun0('x**3 + 4*x**2 - 10')

        result = main.bisection.calculate(function, 1, 2,
                                          tolerance=10**-3)
        self.assertAlmostEqual(result, 1.3647460937)

        with self.assertRaises(main.ConvergenceError):
            main.bisection.calculate(function, 1, 2,
                                     tolerance=10**-3,
                                     max_iterations=2)

        return None
