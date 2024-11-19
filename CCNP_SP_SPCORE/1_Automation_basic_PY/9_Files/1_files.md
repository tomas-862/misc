
## Working with Files

Change to the directory of the file and print the current location along with the files in that location
```python
import os

os.chdir("/mnt/c/Users/OneDrive/Documents/Git/misc/CCNP_SP_SPCORE/Files")
print(os.getcwd())
print()
print(os.listdir())
print()
```

Create a temporary variable "temp" to store the content in a temporary placeholder.
Here "r" indicates read-only mode.
```python
temp = open("R1.cfg", "r")
```

Create a permanent variable "R1_config" to store the content of the previously opened file "R1.cfg".
This will hold the configuration for the R1 router.
```python
R1_config = temp.read()
```

Print the contents of the variable "R1_config"
```python
print(R1_config)
```

This is how I can give read access to the content of the file.
```
