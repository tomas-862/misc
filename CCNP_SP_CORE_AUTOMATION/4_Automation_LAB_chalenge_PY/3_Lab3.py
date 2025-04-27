# Create a script with the file name as Lab3.py. 

# Create a string variables named old_ip_address1 which has the string value as 192.168.100.100. 
# Create a string variables named old_ip_address2 which has the string value as 192.168.200.200.
 
# Use the split and replace built-in methods and replace all occurrences of .100 with .254. 
# Use the split and replace built-in methods and replace the first occurrence of 200 with .254. 
# Once the IP addresses are modified, print the following:
## The old IP addresses are 192.168.1.100 and 192.168.2.200
## The new IP addresses are ['192', '168', 254, '254'] and ['192', '168', 254, '200']


old_ip_address1 = "192.168.100.100"
old_ip_address2 = "192.168.200.200"

temp_ip_address1 = old_ip_address1.replace(".100", ".254", 2)
temp_ip_address2 = old_ip_address2.replace(".200", ".254", 1)

updated_ip_address1 = temp_ip_address1.split(".")
updated_ip_address2 = temp_ip_address2.split(".")

print(f"The old IP addresses are {old_ip_address1} and {old_ip_address2}")
print(f"The new IP addresses are {updated_ip_address1} and {updated_ip_address2}")
