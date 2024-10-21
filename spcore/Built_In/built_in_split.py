# we will use 'split' bult-in  to split variable

# set variable 
IP_Address = "192.168.1.1"

# we will use 'split', in the bracket we define where we want to split. We will at "."
# we will print and will verify type of split variable
print(type(IP_Address))
print(IP_Address.split("."))
print(type(IP_Address.split(".")))
print()
# we can see that split variable is list, not string anymore

# define new variable 'IP_List' and print 3rd list item. 
IP_List = IP_Address.split(".")
print(IP_List[3])