# Introduction:

This program contains several iterative methods for approximating fixed points and roots of single variable functions as well as the root of two. The methods available for finding the root of an equation are the bisection and newton-raphson method. These methods are run using the appropriate subcommand of the program. For help on the arguments expected for each subcommand, use --help and see the examples below.

The primary external dependency of this program is sympy which is used to parse functions provided by the user into computational functions and calculate the first derivative of the function when the newton-raphson method is selected.

# Run Instructions:

## Option 1: An easy way to run the program is from an editable install of the source directory.

To do this:
1. Create a virtual environment in the top level project directory \
`python -m venv .venv`
2. Activate the virtual environment \
`source .venv/bin/activate`
3. Editable install in the directory with the pyproject.toml \
`python -m pip install --editable .`
4. Run the program \
`python -m main ...` (see below for sample inputs)

The program can also be tested from the top level project directory: \
`python -m unittest discover -v -s src`

## Option 2: The program can be run installing only the requirements.txt

To do this:
1. Create a virtual environment in the top level project directory \
`python -m venv .venv`
2. Activate the virtual environment \
`source .venv/bin/activate`
3. Install the requirement packages \
`python -m pip install -r requirements.txt`
4. Run the program from the src directory \
`python -m main ...` (see below for sample inputs)

# Examples:

`python -m main -s --tolerance 0.001 approximation 1.5` \
Result: 1.4142135623

`python -m main -s --tolerance 0.001 bisection "x\*\*3 + 4\*x\*\*2 - 10" 1 2` \
Result: 1.3647460937

`python -m main -s --tolerance 0.001 fixed_point "sqrt(10 - x\*\*3) / 2" 1.5` \
Result: 1.3654100611

`python -m main -s --tolerance 0.001 newton_raphson "cos(x) - x" 0.5` \
Result: 0.7390851339
