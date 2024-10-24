## Nested Object ##
Nested (įdėtas) objects when you combine multiple dictionaries and or List into single variable  
As example lets create a list which contains multiple dictionararies inside

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

Therefore we have single variable (type list), which contains 2 dictionaries inside. 
If we want to print only one of dictionaries, we need to use index 

```python
print(devices[0])

```
