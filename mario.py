# In a file called mario.py in a folder called sentimental-mario-less, write a program that recreates a half-pyramid using hashes (#) for blocks.

# To make things more interesting, first prompt the user with get_int for the half-pyramid’s height, a positive integer between 1 and 8, inclusive.
# If the user fails to provide a positive integer no greater than 8, you should re-prompt for the same again.
# Then, generate (with the help of print and one or more loops) the desired half-pyramid.
# Take care to align the bottom-left corner of your half-pyramid with the left-hand edge of your terminal window.


# promt user for the Height

# import cs50
from cs50 import get_int

while True:
    x = get_int("Height: ")
    y = 9
    if x > 0 and x < y:
        break

counter = 0
while counter < x:
    print("*" *(x - counter), "#" *(counter + 1))
    counter +=1


