import main
import main.newton_raphson
import unittest


class Test_Newton_Raphson(unittest.TestCase):

    def test_calculate(self):

        fstr = 'cos(x) - x'
        function = main.strtofun0(fstr)
        function_prime = main.strtofun1(fstr)

        result = main.newton_raphson.calculate(function, function_prime, 0.5,
                                               tolerance=10**-5)
        self.assertAlmostEqual(result, 0.7390851332)

        with self.assertRaises(main.ConvergenceError):
            main.newton_raphson.calculate(function, function_prime, 0.5,
                                          tolerance=10**-5,
                                          max_iterations=2)

        return None
