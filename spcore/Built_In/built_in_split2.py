# we will make small script and will use '\n'.
# '\n' is a special escape sequence that represents a newline character. 
# When included in a string, it instructs Python to start a new line wherever it appears

show_run = "interface G0/0/0\n no shut\n description Connected to CSR1\n ip address 10.0.0.1 255.255.255.0"
print()
print(show_run)
print()

# we will 'split' our scrip per '/n'
updated_show_run = show_run.split("\n")
print(show_run.split("\n"))
print()

# we can get the same result using 'split.lines' built-in and not using '\n' as split value
updated_show_run = show_run.split("\n")
print(show_run.splitlines())
print()



# This script demonstrates the use of the escape sequence '\n'.
# '\n' is a special escape sequence that represents a newline character. 
# When included in a string, it instructs Python to start a new line wherever it appears.

show_run = "interface G0/0/0\nno shut\ndescription Connected to CSR1\nip address 10.0.0.1 255.255.255.0"
print()
print(show_run)
print()

# We will 'split' our script using '\n' as the delimiter.
updated_show_run = show_run.split("\n")
print(updated_show_run)
print()

# We can achieve the same result using the 'splitlines' built-in method without specifying '\n' as the delimiter.
updated_show_run = show_run.splitlines()
print(updated_show_run)
print()

