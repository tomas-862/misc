List can contain multiple data types in the single list  
i.e. variable type 'List' can have multiple data types in it, separated by comma.  
>>> router = "csr1000v"  
>>> type(router)  
<class 'str'>  
  
>>> version = "16.8"  
>>> type(version)  
<class 'str'>  
  
>>> version = 16.8  
>>> type(version)  
<class 'float'>  
  
>>> description = "This router is a"  
  
>>> info = ["Hello", router, 10, version, description]  
>>> 
>>> type(info)  
<class 'list'>  
>>>>>> if I want to view particular data in the list, you need to give number / position  
>>>  
>>> info[0]  
'Hello'  
  
>>> print(info)  
['Hello', 'csr1000v', 10, 16.8, 'This router is a']  
  
>>> print(info[1])  
csr1000v  
  

if I do '1:' it will print everything from 1 to the end.  
>>> print(info[1:])  
['csr1000v', 10, 16.8, 'This router is a']  
>>>  
If I do '1:3' it will print everything from 1 to 3. Included 1, but not 3 i.e. 1 and 2.  
>>> print(info[1:3])  
['csr1000v', 10]  
>>>  
