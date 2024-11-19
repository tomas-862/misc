## OS Module in Python
The OS module in Python is used to navigate and manipulate directories and files.   

To use the OS module, simply import it as follows:   
```python
import os
```

To check the current working directory (similar to the `pwd` command in the shell), use `os.getcwd()`:
```python
current_directory = os.getcwd()
print(current_directory)
# Example output: '/CCNP_SP_SPCORE/OS_module_py'
```

To change the directory (similar to the `cd` command), use `os.chdir()` and specify the target directory:
```python
os.chdir("/mnt/Documents/Git")
print(os.getcwd())
# Example output: '/mnt/c/Users/tomas/OneDrive/Documents/Git'
```

To create a new directory, use `os.mkdir()`:
```python
os.chdir("/CCNP_SP_SPCORE/OS_module_py")
os.mkdir("test")
print(os.listdir())
# Example output: ['OS_module.md', 'OS_module.py', 'test']
```

To delete a directory, use `os.rmdir()` (note that `os.removedirs()` will remove intermediate directories as well if they are empty):
```python
os.rmdir("test")
print(os.listdir())
# Example output: ['OS_module.md', 'OS_module.py']
```

### Viewing File Contents

To execute a command similar to `cat` using `os.system()`, you can display the contents of a file. Note that `os.system()` is used to execute shell commands and isn't the typical way to read file content in Python:
```python
import os

# The following command will not display file contents directly.
# Instead, you should read the file using Python's file handling.

output = os.system("cat OS_module.py")
print(output)
```
