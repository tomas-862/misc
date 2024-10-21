## we will use built-in 'replace' to replace '.' to ':' in mac address
mac_address = input("Enter mac address in format aa.bb.cc.dd.ee.ff: ")

# using 'replace' we will print out mac address in format aa:bb:....
# built in 'replace' usage is VAR.replace("A" , "C")
# where VAR - variable where to look at. 
# where A - what to replace
# where C - to what to replace
print("mac_address in new format", mac_address.replace("." , ":"))


