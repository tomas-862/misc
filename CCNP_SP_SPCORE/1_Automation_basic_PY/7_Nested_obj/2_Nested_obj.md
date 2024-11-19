## Nested Objects

Nested objects are created when you combine multiple dictionaries and/or lists into a single variable. 

For example, let's create a list that contains multiple dictionaries:

```python
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

```
In this case, we have a single variable of type list that contains two dictionaries. 


To print only one of the dictionaries, we can use its index:
```python
print(devices[0])

```

If we want to print a specific key within a dictionary, we need to specify both the index and the key of the value we want to print:
```python
print(devices[0] ["hostname"])

```


