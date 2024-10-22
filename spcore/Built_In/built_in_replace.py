# We will use the built-in 'replace' method to change '.' to ':' in a MAC address.
mac_address = input("Enter MAC address in the format aa.bb.cc.dd.ee.ff: ")

# Using 'replace', we will print out the MAC address in the format aa:bb:cc:dd:ee:ff.
# The usage of the built-in 'replace' method is as follows:
# VAR.replace("A", "C")
# - VAR: the variable to search in
# - "A": the substring to replace
# - "C": the substring to replace with
print("MAC address in new format:", mac_address.replace(".", ":"))
