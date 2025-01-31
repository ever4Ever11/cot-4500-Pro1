import main
import main.fixed_point
import unittest


class Test_Fixed_Point(unittest.TestCase):

    def test_calculate(self):

        function = main.strtofun0('(x**2 - 1) / 3')

        result = main.fixed_point.calculate(function, 0,
                                            tolerance=10**-4)
        self.assertAlmostEqual(result, -0.3027649777)

        with self.assertRaises(main.ConvergenceError):
            main.fixed_point.calculate(function, 0,
                                       tolerance=10**-4,
                                       max_iterations=2)

        function = main.strtofun0('sqrt(10 - x**3) / 2')

        result = main.fixed_point.calculate(function, 1.5,
                                            tolerance=10**-6)
        self.assertAlmostEqual(result, 1.3652302361)

        function = main.strtofun0('x - x**3 - 4*x**2 + 10')

        with self.assertRaises(OverflowError):
            main.fixed_point.calculate(function, 1.5,
                                       tolerance=10**-6)

        return None
