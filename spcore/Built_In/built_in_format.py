# create variables
ccie2 = "CCIE Security"
num_of_sec = input("How many CCIE Sec certified people: ")

# create variable 'total_sec' with 2x {} in which I can specify variables
total_sec = "There are {} {} certified people in the world\n"

# will use buil-in 'format' and insert variables to hte {} of the variable 'total_sec'
print(total_sec.format (num_of_sec, ccie2))