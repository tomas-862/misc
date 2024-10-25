## OS module in Python  
To navigate and manipulate direcotries and files we use OS module  

Install OS module in Python  
```python
import OS
```

To check current workign directory (same as we use PWD) we use "get" and "cwd" (current working direcotry) under "os".  
```python
os.getcwd()
print(os.getcwd())
# output: '/mnt/c/Users/tomas/OneDrive/Documents/Git/misc/CCNP_SP_SPCORE/OS_module_py'
```

to change dir (same as we use CD) we use "chdir" under "os and define target directory.  
```python
os.chdir("/mnt/c/Users/tomas/OneDrive/Documents/Git")
print (os.getcwd())
# output: '/mnt/c/Users/tomas/OneDrive/Documents/Git'
```

to make new dir we use 'os.mkdir' 
```python
os.chdir("/mnt/c/Users/tomas/OneDrive/Documents/Git/misc/CCNP_SP_SPCORE/OS_module_py")
os.mkdir ("test")
print(os.listdir())
print()
# output: '['OS_module.md', 'OS_module.py', 'test']' 
```

to delete direcotry we use 'os.removedirs'  
```python
os.removedirs("test")
print(os.listdir())
print()
# output: '['OS_module.md', 'OS_module.py']'
```

to view file with 'os'' module using 'cat' 
```python
print(os.system("OS_module.py"))
# output: //// content of thr file //// '
```

