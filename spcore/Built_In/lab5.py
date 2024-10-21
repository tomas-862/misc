# create a var string "ccie" with value "CCIE Enterprise Infrasttucture\n"
ccie = "CCIE Enterprise Infrastructure\n"

# create a var string "ip_address1" value "10.1.2.100"
ip_address1 = "10.1.2.100"

# create a var string "ip_address2" value "10.3.4.200"
ip_address2 = "10.3.4.200"

# store  var "ccie" in the new var called "lower_ccie". Value must be in lower case.
lower_ccie = ccie.lower()

# split content of ip_address1 to the list called "new_ip_address1"
new_ip_address1 = ip_address1.split(".")

# split content of ip_address2 to the list called "new_ip_address2"
new_ip_address2 = ip_address2.split(".")

# split contect of "lower_ccie" into the list "new_lower_ccie"
new_lower_ccie = lower_ccie.split()

# print 3rd octet of "new_ip_address1"
print(new_ip_address1[2])

# print 4th octet of "new_ip_address2"
print(new_ip_address2[3])

# print "new_lower_ccie"
print(new_lower_ccie)

