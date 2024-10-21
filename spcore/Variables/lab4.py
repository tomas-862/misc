# Define variables
ccie1 = "CCIE Enterprise Infrastructure"
ccie2 = "CCIE Service Provider"
ccie3 = "CCIE Security"
ccie4 = "CCIE Collaboration"
ei = "40000"
sp = "10000"
sec = "15000"

# Convert strings to integers
ei_int = int(ei)
sp_int = int(sp)
sec_int = int(sec)

# Sum the integers
total = ((ei_int + sp_int) + sec_int)

# Create f-strings
total_ei = f"There are {ei} {ccie1} certified people in the world"
total_sp = f"There are {sp} {ccie2} certified people in the world"
total_sec = f"There are {sec} {ccie3} certified people in the world"  # Changed to ccie3
total_ccie = f"The total number of CCIEs in the world is {total}"

# Print out 
print(total_ei)
print(total_sp)
print(total_sec)
print()
print(total_ccie)
