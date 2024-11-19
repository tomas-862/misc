
# Example 1
devices = ["R1", "R2", "R3", "R4", "FW1"]
for item in devices:
    print(item)

print()
    
# Example 2

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

    

