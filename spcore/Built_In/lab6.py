# create var "ip_address" with value "10.1.5.5."
ip_address = "10.1.5.5"

# with built-in 'replace' replace '5' with '2' and store in new var "temp_ip_address"
temp_ip_address = ip_address.replace("5" , "2")
print(temp_ip_address)

# with 'replace' built-in replace 1st occurance of '2' with 100 and store as "new_ip_address"
new_ip_address = temp_ip_address.replace("2", "100", 1)

# create var "csr_ip_address" with value "The IP address of the gateway router is {}"
csr_ip_address = "The IP address of the gateway router is {}"

# print csr router address is 10.1.100.2
print(csr_ip_address.format(new_ip_address))
