# We will use the built-in 'split' method to split a variable.

# Set the variable for the IP address
IP_Address = "192.168.1.1"

# We will use 'split' to divide the string at each occurrence of the "." character.
# We will print the original type of the variable and the result of the split operation.
print(type(IP_Address))  # Output the type of the original variable
print(IP_Address.split("."))  # Print the result of splitting the IP address
print(type(IP_Address.split(".")))  # Output the type of the result after splitting
print()

# We can see that the result of the split operation is a list, not a string anymore.

# Define a new variable 'IP_List' and print the 4th item (index 3) from the list.
IP_List = IP_Address.split(".")
print(IP_List[3])  # Output the 4th item in the list
