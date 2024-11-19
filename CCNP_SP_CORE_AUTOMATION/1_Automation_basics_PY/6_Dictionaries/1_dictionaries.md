### Dictionaries in Python
Dictionaries in Python are unordered collections that store items as key-value pairs. Unlike lists, which are indexed by numbers, items in a dictionary are accessed by their keys.


#### Defining a List (refresh)
We can define the list as follow:
```python
list1 = [
    "R1",
    "10.1.1.1",
    "IOS-XE",
    "16.8"
]
```
We can print the list:
```python
print(list1)  
# Output: ['R1', '10.1.1.1', 'IOS-XE', '16.8']
```
To print an item from the list, you need to use its index:
```python
print(list1[1])  
# Output: '10.1.1.1'
```


#### Creating a Dictionary
Dictionaries are created using curly braces `{}`. You define a key (e.g., `"Hostname"`) and assign it a value (e.g., `"R1"`). Keys and values are separated by a colon `:`.
```python
dict1 = {
    "Hostname": "R1",
    "Mgmt-IP": "10.1.1.1",
    "Image": "IOS-XE",
    "Version": "16.8"
}
```
You can check the contents of the dictionary:
```python
print(dict1)  
# Output: {'Hostname': 'R1', 'Mgmt-IP': '10.1.1.1', 'Image': 'IOS-XE', 'Version': '16.8'}
```

To confirm the type of `dict1`:
```python
print(type(dict1))  
# Output: <class 'dict'>
```

#### Accessing Values
You can access values in the dictionary using their keys:
```python
print(dict1["Mgmt-IP"])  
# Output: 10.1.1.1
```


#### Another Way to Create a Dictionary
You can also create an empty dictionary and add key-value pairs one by one:
```python
dict1 = {}
dict1["Hostname"] = "R1"
dict1["Mgmt-IP"] = "10.1.1.1"
dict1["Image"] = "IOS-XE"
dict1["Version"] = "16.8"
```
Check the contents of the dictionary:
```python
print(dict1)  
# Output: {'Hostname': 'R1', 'Mgmt-IP': '10.1.1.1', 'Image': 'IOS-XE', 'Version': '16.8'}
```


#### Adding New Item
You can easily add new items to the dictionary:
```python
dict1["Mgmt-Interface"] = "G0/0/0/"
print(dict1)  
# Output: {'Hostname': 'R1', 'Mgmt-IP': '10.1.1.1', 'Image': 'IOS-XE', 'Version': '16.8', 'Mgmt-Interface': 'G0/0/0/'}
```

#### Printing Keys and Values
To print only the keys of the dictionary, use the `keys()` method:
```python
print(dict1.keys())  
# Output: dict_keys(['Hostname', 'Mgmt-IP', 'Image', 'Version', 'Mgmt-Interface'])
```

To print just the values, use the `values()` method:
```python
print(dict1.values())  
# Output: dict_values(['R1', '10.1.1.1', 'IOS-XE', '16.8', 'G0/0/0/'])
```


#### Merging Dictionaries
You can create another dictionary and merge it with the first one:
```python
dict2 = {}
dict2["Hostname"] = "R2"
dict2["Mgmt-IP"] = "10.1.1.2"
```

Check the contents of both dictionaries:

```python
print(dict1)  
# Output: {'Hostname': 'R1', 'Mgmt-IP': '10.1.1.1', 'Image': 'IOS-XE', 'Version': '16.8', 'Mgmt-Interface': 'G0/0/0/'}

print(dict2)  
# Output: {'Hostname': 'R2', 'Mgmt-IP': '10.1.1.2'}
```

Update `dict1` with the values from `dict2`:
```python
dict1.update(dict2)
print(dict1)  
# Output: {'Hostname': 'R2', 'Mgmt-IP': '10.1.1.2', 'Image': 'IOS-XE', 'Version': '16.8', 'Mgmt-Interface': 'G0/0/0/'}
```

**Note:** If the same key exists in both dictionaries, the value in the second dictionary will overwrite the value in the first. In the example above, the hostname value `"R1"` was overwritten with `"R2"` because `"Hostname"` was present in both `dict2` and `dict1`.




#### Removing Key-Value Pairs
To remove a key-value pair from a dictionary, you can use the `pop` method. For example, to remove `"Hostname"` from `dict1`:
```python
dict1.pop("Hostname")  
# Output: 'R2'
```

After executing this, if you print `dict1`, it will no longer contain the `"Hostname"` key.


#### Accessing Values with `get`
You can access the value of a specific key using both bracket notation and the `get` method. 

Using bracket notation:
```python
print(dict1["Mgmt-IP"])  
# Output: '10.1.1.2'
```

Using the `get` method:
```python
print(dict1.get("Mgmt-IP"))  
# Output: '10.1.1.2'
```

The difference between these two methods is that using `get` will not raise an error if the key does not exist.

For example, if you try to access a nonexistent key:
```python
dict1.get("Hostname")  
# Output: None
```

If you use bracket notation to access a nonexistent key, it will raise a `KeyError`:
```python
print(dict1["Hostname"])  
# Output: KeyError: 'Hostname'
```


#### Providing Default Values with `get`
You can also use the `get` method to print a message if the key does not exist in the dictionary. For instance:
```python
print(dict1.get("Hostname2", "This key doesn't exist"))  
# Output: 'This key doesn't exist'
```

Moreover, if you want to check if a key exists and provide a default message:
```python
print(dict1.get("Hostname"))  
# Output: None (since "Hostname" was removed)

print(dict1.get("Hostname", "This doesn't exist"))  
# Output: 'This doesn't exist'
```
