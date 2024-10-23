###dictionaries in py###  
dictionaries are unordered list, items in dic are not indexed by number but by name, which are refered as key.  
  
We define list as follow:  
>>> list1 = [  
    "R1",  
    "10.1.1.1",  
    "IOS-XE",  
    "16.8"  
    ]  
We can print list  
>>> list1  
['R1', '10.1.1.1', 'IOS-XE', '16.8']  
>>>  
If I want print item of the list, I need to define index number  
>>> list1[1]  
'10.1.1.1'  
>>>
  
to create dictionaries we will use curley brackets {}, then we will give key / name e.g.   "Hostname", then we special a value e.g.  "R1". key and value separated by column.   
  
>>> dict1 = {"Hostname": "R1", "Mgmt-IP": "10.1.1.1", "Image": "IOS-XE", "Version": "16.8"}  
>>> dict1  
{'Hostname': 'R1', 'Mgmt-IP': '10.1.1.1', 'Image': 'IOS-XE', 'Version': '16.8'}   
>>>  
>>> type(dict1)  
<class 'dict'>  
>>>  
If I want to call /print value I can do based name not on number e.g. I want to print Mngm-IP  
>>> print(dict1["Mgmt-IP"])
10.1.1.1
>>>
