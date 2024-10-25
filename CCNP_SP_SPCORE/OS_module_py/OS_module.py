# import 'os' module
import os

# check current dir (PWD)
os.getcwd()
print(os.getcwd())
print()

# change dir to "Git" and print. 
os.chdir("/mnt/c/Users/tomas/OneDrive/Documents/Git")
print (os.getcwd())


# navigate to direcotry "OS_module_py", create dir "test", print out list of all the files in the dirdorectory to ensire "test" is here.
os.chdir("/mnt/c/Users/tomas/OneDrive/Documents/Git/misc/CCNP_SP_SPCORE/OS_module_py")
os.mkdir ("test")
print(os.listdir())
print()
# output: '['OS_module.md', 'OS_module.py', 'test']'  

# remove "test" dir and print the list to ensure diroctory is deleted.  
os.removedirs("test")
print(os.listdir())
print()

# print out file contecnt with using 'os' with 'cat'
print(os.system("cat OS_module.py"))
