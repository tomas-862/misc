## For Loop in Python

The `for` loop allows you to iterate over a sequence (such as a list) and execute a block of code repeatedly.

### Example 1: Iterating Through a List of Devices

Let's say you have a list called `devices`, which contains the names of your routers, such as "R1", "R2", etc. You can use a `for` loop to print each device until the list is fully iterated.

```python
devices = ["R1", "R2", "R3", "R4", "FW1"]
for item in devices:
    print(item)
# Output: 
# R1
# R2
# R3
# R4
# FW1
```

In the example above, we demonstrate how easy it is to print out all devices using a `for` loop. This can be particularly useful when you need to perform actions on multiple devices in network automation scripts.

### Example 2: Using Conditions with a For Loop

In addition to simple iteration, you can also incorporate conditions within a `for` loop to execute specific actions based on the item's characteristics. For instance, consider you have a list of interfaces, and you want to categorize them based on their naming conventions.

```python
interfaces = ["GigabitEthernet1/1", "Loopback0", "GigabitEthernet1/2", "TenGigabitEthernet1/1", "Vlan100"]
for item in interfaces:
    if item.lower().startswith("gig"):
        int_type = "Giga"
    elif item.lower().startswith("loop"):
        int_type = "Loopback"
    elif item.lower().startswith("vlan"):
        int_type = "Vlan"
    else:
        int_type = "Unknown"
    print(f"Interface type of {item} is {int_type}")
# Output:
# Interface type of GigabitEthernet1/1 is Giga
# Interface type of Loopback0 is Loopback
# Interface type of GigabitEthernet1/2 is Giga
# Interface type of TenGigabitEthernet1/1 is Unknown
# Interface type of Vlan100 is Vlan
```

We use a `for` loop to categorize each interface based on its name. By setting conditions, we can classify the interfaces into types such as Giga, Loopback, Vlan, or Unknown, and then print the interface type for each item. This demonstrates the flexibility of the `for` loop in managing and processing network data efficiently.

