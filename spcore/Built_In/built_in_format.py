# Create variables for CCIE certification and the number of certified individuals
ccie2 = "CCIE Security"
num_of_sec = input("How many CCIE Security certified people are there? ")

# Create a variable 'total_sec' that includes placeholders for formatting
total_sec = "There are {} {} certified people in the world.\n"

# Use the built-in 'format' method to insert variables into the placeholders of 'total_sec'
print(total_sec.format(num_of_sec, ccie2))
