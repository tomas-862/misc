# Let's create a list that contains multiple dictionaries:
devices = [
    {
        "hostname": "R1", "mgm-ip": "10.1.1.1", "Vendor": "cisco", "model": "CSR100"
        },
        {
        "hostname": "R2", "mgm-ip": "10.1.1.2", "Vendor": "cisco", "model": "CSR100"
    }
        ]
type(devices)
len(devices)
print(devices)
print()

# To print only one of the dictionaries, we can use its index:
print(devices[0])
print()
# If we want to print a specific key within a dictionary,
# we need to specify both the index and the key of the value we want to print:
print(devices[0] ["hostname"])
print()
