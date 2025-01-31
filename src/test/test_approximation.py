import main
import main.approximation
import unittest


class Test_Approximation(unittest.TestCase):

    def test_calculate(self):

        result = main.approximation.calculate(1.5,
                                              tolerance=10**-6)
        self.assertAlmostEqual(result, 1.4142135623)

        with self.assertRaises(main.ConvergenceError):
            main.approximation.calculate(1.5,
                                         tolerance=10**-6,
                                         max_iterations=2)

        return None
