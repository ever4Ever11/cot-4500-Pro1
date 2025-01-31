import argparse
import logging
import main
import main.approximation
import main.bisection
import main.fixed_point
import main.newton_raphson
import sys


parser = argparse.ArgumentParser()
parser.add_argument('-t', '--tolerance',
                    default=10**-5,
                    type=float,
                    help='halting tolerance of the calculation')
parser.add_argument('-m', '--max_iterations',
                    default=25,
                    type=int,
                    help='max iterations before the calculation halts')
parser.add_argument('-s', '--steps',
                    action='store_true',
                    help='shows the steps of the calculation')
subparsers = parser.add_subparsers(dest='command',
                                   required=True,
                                   help='selects the numerical method')


subparser = subparsers.add_parser('approximation',
                                  help='calculates the root of 2')
subparser.add_argument('initial_value',
                       type=float,
                       help='initial value of the search')


subparser = subparsers.add_parser('bisection',
                                  help='calculates the function root')
subparser.add_argument('function',
                       help='single variable function with respect to x')
subparser.add_argument('a',
                       type=float,
                       help='left most value of the interval')
subparser.add_argument('b',
                       type=float,
                       help='right most value of the interval')


subparser = subparsers.add_parser('fixed_point',
                                  help='calculates the function fixed point')
subparser.add_argument('function',
                       help='single variable function with respect to x')
subparser.add_argument('initial_value',
                       type=float,
                       help='initial value of the search')


subparser = subparsers.add_parser('newton_raphson',
                                  help='calculates the function root')
subparser.add_argument('function',
                       help='single variable function with respect to x')
subparser.add_argument('initial_value',
                       type=float,
                       help='initial value of the search')


args = parser.parse_args()


logger = logging.getLogger()
logger.setLevel(logging.DEBUG if args.steps else logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))


try:

    if args.command == 'approximation':

        r = main.approximation.calculate(args.initial_value,
                                         tolerance=args.tolerance,
                                         max_iterations=args.max_iterations)

    elif args.command == 'bisection':

        function = main.strtofun0(args.function)

        r = main.bisection.calculate(function, args.a, args.b,
                                     tolerance=args.tolerance,
                                     max_iterations=args.max_iterations)

    elif args.command == 'fixed_point':

        function = main.strtofun0(args.function)

        r = main.fixed_point.calculate(function, args.initial_value,
                                       tolerance=args.tolerance,
                                       max_iterations=args.max_iterations)

    elif args.command == 'newton_raphson':

        function = main.strtofun0(args.function)
        function_prime = main.strtofun1(args.function)

        r = main.newton_raphson.calculate(function, function_prime,
                                          args.initial_value,
                                          tolerance=args.tolerance,
                                          max_iterations=args.max_iterations)

    logger.info(f'Result: {r}')

except ZeroDivisionError as e:
    logger.info(e)
except main.ConvergenceError as e:
    logger.info(e)
except OverflowError:
    logger.info('calculation likely diverged')
except Exception:
    logger.info('unknown error, check your inputs are appropriate')
