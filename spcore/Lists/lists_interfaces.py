# Create a list named "interface1"
interface1 = [
    "description Configured by Python", 
    "switchport mode access", 
    "switchport access vlan 10"
]
print(interface1)

# We can use built-in functions to add additional data to the list. Lists can contain multiple data types.
# We will use the 'append' function to add an item to the end of the list.
interface1.append("no shut")
print(interface1)
print()

# To print different data from the list, we use the index corresponding to the item's position in the list.
print(interface1[2])      # Access the item at index 2
print(interface1[2:])     # Print all items from index 2 to the end
print(interface1[1:3])    # Print items from index 1 to 3 (excluding index 3)
print()

# If we want to add new data at a specific position in the list (not just at the end), we can use the built-in function 'insert'.
# Here, we will add the string "duplex full" at position 1 in the list.
interface1.insert(1, "duplex full")
print(interface1)
print()

# We can remove the last item from the list using the built-in 'pop' function without any arguments.
# Let's remove the last entry, which is 'no shut'.
interface1.pop()
print(interface1)
print()

# We can also extend an existing list with the data we have in another list.
# Let's create a new list named 'basic' and extend it with the data from the list 'interface1'.
# We will use the 'extend' built-in function for this purpose.
basic = ["configure terminal", "interface G0/0/0"]
basic.extend(interface1)
print(basic)

# If we want to change the value of a specific item in the list, we can do so by specifying its index and the updated value.
# We can change "interface G0/0/0" to "interface G0/0/1" in the list.
print(basic)
basic[1] = "interface G0/0/1"
print(basic)
