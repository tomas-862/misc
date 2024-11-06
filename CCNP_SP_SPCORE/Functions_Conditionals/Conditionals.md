
# Using Conditionals in Python

Conditional statements allow us to execute specific actions in our code based on whether certain conditions are true. In this example, we'll check the operating system of individual routers and print the management IP address if the operating system is `IOS-XE`.

## Example: Conditional Logic with Device Information

### Define Device Information

We will define two separate dictionaries, each representing a router.

```python
# Define dictionary for each device.
device1 = {'hostname': 'R1', 'os': 'IOS-XE', 'mgmt-ip': '10.1.1.1'}
device2 = {'hostname': 'R2', 'os': 'IOS-XR', 'mgmt-ip': '10.2.1.1'}
```

### Conditional Logic for Each Device

Now we will implement the conditional logic for each device to check the operating system.

```python
# Check the first device (device1)
if device1['os'] == 'IOS-XE':
    # If true, print the management IP.
    print(f"The management IP for device {device1['hostname']} is {device1['mgmt-ip']}")
else:
    # Otherwise, print that the device is not running 'IOS-XE'.
    print(f"{device1['hostname']} is not running IOS-XE. It is running {device1['os']}.")

# Check the second device (device2)
if device2['os'] == 'IOS-XE':
    # If true, print the management IP.
    print(f"The management IP for device {device2['hostname']} is {device2['mgmt-ip']}")
else:
    # Otherwise, print that the device is not running 'IOS-XE'.
    print(f"{device2['hostname']} is not running IOS-XE. It is running {device2['os']}.")
```

### Example Output

Running the above code will produce the following output:

```
The management IP for device R1 is 10.1.1.1
R2 is not running IOS-XE. It is running IOS-XR.
```

This example demonstrates how to utilize conditional statements to evaluate operating systems of different devices and take appropriate actions based on those evaluations, without using loops.