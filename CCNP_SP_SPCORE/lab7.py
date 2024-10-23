# Create file named lab7.py
# Create var "ip_address" with value "10.1.5.5"
# Create var "interface" value "G0/0/0"
# # Create var "List" with index 0 is var "interface", index 1 is var "ip_address", 
# # index 2 is seet as "desciption connected via Python", index 3 set as "shut"
# print each index value as separate line
# print List
# Modidy List index value 3 with "no shut"
# Print "The IP address of the router is 10.1.5.5" and management interface is G0/0/0"

ip_address = "10.1.5.5"
interface = "G0/0/0"
List = [interface, ip_address, "decription connected via Python", "shut"]

# printing in separate line
print(List[0])
print(List[1])
print(List[2])
print(List[3])
print()

# printing in separate line in more nice way
for item in List:
    print(item)
print()

# printing all list in single line
print(List)
print()

# Modify "shut" to "no shut"
List[3] = "no shut"

# Print final output 
print(f"The IP address of the router is {List[1]} and management interface is {List[0]}")