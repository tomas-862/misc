
### Argparse

When using the `input` function in Python, we must run our Python script, provide input, and then the code executes based on that input.

With `sys.argv`, we can provide inputs in advance, before running the code. In this case, our input will be processed when the code is executed. However, when using `sys.argv`, users need to know which index corresponds to which argument (e.g., first provide the name, then the age, or vice versa). 

With `argparse`, we can go further by seeing all the arguments we need to provide and in which order, which helps us supply the correct command-line arguments.

Let’s see a simple example to understand how to use `argparse`.

```python
import argparse  # Importing the argparse module to handle command-line arguments

parser = argparse.ArgumentParser(description="container")  # Creating an ArgumentParser object with a brief description

# Adding positional arguments for three integers
parser.add_argument("num1", type=int, help="This is integer No 1")  # First integer input
parser.add_argument("num2", type=int, help="This is integer No 2")  # Second integer input
parser.add_argument("num3", type=int, help="This is integer No 3")  # Third integer input

args = parser.parse_args()  # Parsing the command-line arguments given by the user

# Printing the values of the input arguments
print(f"{args.num1} is Integer No 1")  # Output for first number
print(f"{args.num2} is Integer No 2")  # Output for second number
print(f"{args.num3} is Integer No 3")  # Output for third number

# NOTE: When executing the .py file, you can always use '-h' to get help for command line arguments. 
# NOTE: Positional arguments mean that arguments must be in a specific order.

# Output (for '-h'): 
# > python3 .\argparse_basic.py -h   
# usage: argparse_basic.py [-h] num1 num2 num3
#
# container
# positional arguments:
#  num1        This is integer No 1
#  num2        This is integer No 2
#  num3        This is integer No 3
# 
# options:
#  -h, --help  show this help message and exit
# > 

# Output: 
# > python3 .\argparse_basic.py 11 33 12
# 11 is Integer No 1
# 33 is Integer No 2
# 12 is Integer No 3
# > 
```

### Adding Calculation Functionality

We can enhance our script to include a calculation argument that allows the user to perform arithmetic operations. Let’s see an example with calculation capabilities:

```python
import argparse

parser = argparse.ArgumentParser(description="container")

parser.add_argument("num1", type=int, help="This is integer No 1")
parser.add_argument("num2", type=int, help="This is integer No 2")
parser.add_argument("num3", type=int, help="This is integer No 3")
parser.add_argument("calc", help="This will perform a calculation. Use 'add', 'subtract', or 'multiply' arguments for math operations.")  # Operation choice

args = parser.parse_args()

# Assigning input values to variables
n1 = int(args.num1)  # First number
n2 = int(args.num2)  # Second number
n3 = int(args.num3)  # Third number
result = None  # Initializing result variable to store calculation results

# Conditional statements to perform the requested calculation
if args.calc == "add":  # Check if the operation is addition
    result = n1 + n2 + n3  # Calculate the sum of three numbers
elif args.calc == "subtract":  # Check if the operation is subtraction
    result = n1 - n2 - n3  # Calculate the difference
elif args.calc == "multiply":  # Check if the operation is multiplication
    result = n1 * n2 * n3  # Calculate the product
else:  # If the operation is not recognized
    print("Invalid operation option. Please use 'add', 'subtract', or 'multiply'.")  # Inform the user of the error
    exit()  # Exit if there's an invalid calculation option

print(result)

# Output (for '-h'): 
# > python3 .\argparse_basic2.py -h             
# usage: argparse_basic2.py [-h] num1 num2 num3 calc
# 
# container
# 
# positional arguments:
#  num1        This is integer No 1
#  num2        This is integer No 2
#  num3        This is integer No 3
#  calc        This will perform a calculation. Use 'add', 'subtract', or 'multiply' arguments for math operations.
#
# options:
#   -h, --help  show this help message and exit
# > 

# Output: 
# > python3 .\argparse_basic2.py 1 2 3 add
# 6
# > python3 .\argparse_basic2.py 1 2 3 subtract
# -4
# > python3 .\argparse_basic2.py 1 2 3 multiply 
# 6
# > 

