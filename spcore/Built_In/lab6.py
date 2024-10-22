# Create a variable 'ip_address' with the value "10.1.5.5"
ip_address = "10.1.5.5"

# Use the built-in 'replace' method to replace '5' with '2' and store the result in a new variable 'temp_ip_address'
temp_ip_address = ip_address.replace("5", "2")
print(temp_ip_address)  # Output: "10.1.2.2"

# Replace the first occurrence of '2' with '100' using 'replace' and store the result as 'new_ip_address'
new_ip_address = temp_ip_address.replace("2", "100", 1)

# Create a variable 'csr_ip_address' with a formatted string
csr_ip_address = "The IP address of the gateway router is {}"

# Print the formatted message with the new IP address
print(csr_ip_address.format(new_ip_address))  # Output: "The IP address of the gateway router is 10.1.100.2"
