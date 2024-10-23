# Create a variable 'ccie' with a multiline string containing different CCIE tracks.
ccie = "CCIE Enterprise Infrastructure\nCCIE Service Provider\nCCIE Security"

# Create a variable 'ip_address1' with the value "10.1.2.100"
ip_address1 = "10.1.2.100"

# Create a variable 'ip_address2' with the value "10.3.4.200"
ip_address2 = "10.3.4.200"

# Convert the content of 'ccie' to lowercase and store it in a new variable called 'lower_ccie'.
lower_ccie = ccie.lower()

# Split the content of 'ip_address1' into a list called 'new_ip_address1'.
new_ip_address1 = ip_address1.split(".")

# Split the content of 'ip_address2' into a list called 'new_ip_address2'.
new_ip_address2 = ip_address2.split(".")

# Split the content of 'lower_ccie' into a list called 'new_lower_ccie'.
new_lower_ccie = lower_ccie.split()

# Print the 3rd octet of 'new_ip_address1'.
print(new_ip_address1[2])  # Output: 2

# Print the 4th octet of 'new_ip_address2'. Note that list indexing starts at 0.
print(new_ip_address2[2])  # Output: 200

# Print the list 'new_lower_ccie'.
print(new_lower_ccie)
