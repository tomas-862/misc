## For Loop
If I want to make something repeatedly until conditions happeniong I can use so called "For Loop".

For example if I have a list "devices" where I have listed my routers "R1", "R2" etc. 
I can you For Loop to print this list until its empties. 

```python 
devices = ["R1", "R2", "R3", "R4", "FW1"]
for item in devices:
    print(item)
# Output: 
# R1
# R2
# R3
# R4
# FW
```
In above example we see how easy print out all devices using For lopp. 

Another example where we use for loop with conditions and set the action. We have a list of interface and using for loop we will set interface depending on interface name. 

```python
interfaces = ["GigabitEthernet1/1", "Loopback0", "GigabitEthernet1/2", "TenGigabitEthernet1/1,", "Vlan100"]
for item in interfaces:
    if item.lower().startswith("gig"):
        int_type = "Giga"
    elif item.lower().startswith("loop"):
        int_type = "Loopback"
    elif item.lower().startswith("vlan"):
        int_type = "Vlan"
    else:
        int_type = "Unk"
    print (f"Interface type of {item} is {int_type}")
# Output:
# Interface type of GigabitEthernet1/1 is Giga
# Interface type of Loopback0 is Loopback
# Interface type of GigabitEthernet1/2 is Giga
# Interface type of TenGigabitEthernet1/1, is Unk
# Interface type of Vlan100 is Vlan
```

In above exmaple we forloopoing our list of interfaces, by condition assigning them interface type and then print them. 
    
