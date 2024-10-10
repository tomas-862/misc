# In a file called cash.py, write a program that asks the user how much change is owed
# and then spits out the minimum number of coins with which said change can be made.

# Use get_float from the CS50 Library to get the user’s input and print to output your answer.
# Assume that the only coins available are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢).

# We ask that you use get_float so that you can handle dollars and cents, albeit sans dollar sign.
# In other words, if some customer is owed $9.75 (as in the case where a newspaper costs 25¢ but the customer pays with a $10 bill),
# assume that your program’s input will be 9.75 and not $9.75 or 975. However, if some customer is owed $9 exactly, assume that your program’s input will be 9.00 or just 9 but, again, not $9 or 900.
# Of course, by nature of floating-point values, your program will likely work with inputs like 9.0 and 9.000 as well; you need not worry about checking whether the user’s input is “formatted” like money should be.

# If the user fails to provide a non-negative value, your program should re-prompt the user for a valid amount again and again until the user complies.
# Incidentally, so that we can automate some tests of your code, we ask that your program’s last line of output be only the minimum number of coins possible: an integer followed by a newline.


# Import cs50
from cs50 import get_float

# Define constant variables (coin values in cents)
a = 25  # quarters
b = 10  # dimes
c = 5   # nickels
d = 1   # pennies
i = 0   # counter for coins

# Get user input
while True:
    x = get_float("Change: ")
    if x > 0:
        break

# Convert dollars to cents
x = int(x * 100)

# Calculate the number of coins
while x > 0:
    while x >= a:
        x -= a  # Subtract the value of the coin
        i += 1  # Increment the coin counter

    while x >= b:
        x -= b
        i += 1

    while x >= c:
        x -= c
        i += 1

    while x >= d:
        x -= d
        i += 1

# Output the total number of coins
print(i)



