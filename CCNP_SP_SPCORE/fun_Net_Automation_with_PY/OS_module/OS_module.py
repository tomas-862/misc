
import os

# Get current working directory
# This function returns the current working directory, similar to the `pwd` command in UNIX.
current_directory = os.getcwd()
print(current_directory)  # Example output: '/mnt/c/Users/AAA/OneDrive/Documents/Git/misc/CCNP_SP_SPCORE/OS_module_py'

# Change the current working directory
# This action is equivalent to using `cd` in the command line. 
# Specify the target directory to switch to.
os.chdir("/mnt/c/Users/AAA/OneDrive/Documents/Git")
print(os.getcwd())  # Example output: '/mnt/c/Users/AAA/OneDrive/Documents/Git'

# Create a new directory
# This function creates a directory with the specified name in the current working directory.
os.chdir("/mnt/c/Users/AAA/OneDrive/Documents/Git/misc/CCNP_SP_SPCORE/OS_module_py")
os.mkdir("test")
print(os.listdir())  # Example output: ['OS_module.md', 'OS_module.py', 'test']

# Delete the newly created directory
# This function removes the specified directory. Note that the directory must be empty before it can be deleted.
os.rmdir("test")
print(os.listdir())  # Example output: ['OS_module.md', 'OS_module.py']

# Viewing file contents using os.system
# The following command will execute a shell command. 
# While `os.system()` can be used to run commands like `cat`, it is not the most efficient way to read a file's contents in Python.
output = os.system("cat OS_module.py")  # Note: Replace with a more appropriate method for reading files if needed.
print(output)

# A better way to read and display file contents in Python
# Use built-in file handling functions to read the contents of a file as shown below.
with open("OS_module.py", "r") as file:
    content = file.read()
    print(content)  # Output: Displays the content of 'OS_module.py'
