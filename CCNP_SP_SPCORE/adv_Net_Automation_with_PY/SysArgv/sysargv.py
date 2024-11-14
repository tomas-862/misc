

import sys  # Import the sys module

# Check if the correct number of command-line arguments is provided
if len(sys.argv) < 3:  # If fewer than 3 arguments (script name + name + age)
    print("Usage: python script_name.py <name> <age>")  # Print usage message
    sys.exit(1)  # Exit the script with a non-zero status

name = sys.argv[1]  # Get the first command-line argument (name)
age = sys.argv[2]   # Get the second command-line argument (age)
print(f"My name is {name} and my age is {age}")  # Output the name and age
