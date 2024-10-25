# import 'os' module
import os

# check current dir (PWD)
os.getcwd()
print(os.getcwd())
print()

# change dir to "Git" and print. 
os.chdir("C:/Users/tomas/OneDrive/Documents/Git")
print (os.getcwd())

# navigate to direcotry "OS_module_py", create file "test.txt", print out list of all the files in the dirdorectory to ensire test.txt is here.
os.chdir("C:/Users/tomas/OneDrive/Documents/Git/misc/CCNP_SP_SPCORE/OS_module_py")
os.mkdir ("test.txt")
print(os.listdir())


