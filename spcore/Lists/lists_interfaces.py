# create a list "interface1"
interface1 = ["description Configured by Python", "switchport mode access", "switchport access vlan 10"]
print(interface1)

# we can use built-in functions to add additional data in the list. List can have multiple data types. 
# we will use 'append' funciton
interface1.append("no shut")
print(interface1)
print()

#printing different data from the list, we use number of the data position in the list.
print(interface1[2])
print(interface1[2:])
print(interface1[1:3])
print()

# if we want to add new data to the list somewhere not in the end, I can use buil-in funcion 'insert' 
# we will add new string "duplex full" int he position 1 of the list 
interface1.insert(1, "duplex full")
print(interface1)
print()

# we can remove last item from the list using built-in 'pop' with no value
# lets remove last data 'no shut'
interface1.pop()
print(interface1)
print()

# we can extend existing list with data we have in another string. 
# lets create new list 'basic' and extend it with data we have in the list 'interface1' 
# we will use 'extend' built-in funcion. 
basic = ["configure terminal", "interface G0/0/0"]
basic.extend(interface1)
print(basic)

# if we want to change value of data in the list it is easy to change by defining sequence number and updated data
# we can change "interface G0/0/0" to "interface G0/0/1" in the list
print(basic)
basic[1] = "interface G0/0/1"
print(basic)