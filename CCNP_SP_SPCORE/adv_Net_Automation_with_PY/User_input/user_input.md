# User Input   

We can use funcion "input" to ask user for the input. User respond will be string, so if we want to have user respond as integer, we can change type of variable to integer and some math with. 
Let look at basic example below. 

```python
# We will use funcion "input" to get user input
switches = input("How many switches: ") 
print(type(switches)) # we print type of variable 
print()

# changing to integer
num_switches = int(switches)
print(type(num_switches)) # we print type of variable  
print()

# We can do some math with our new integer e.g. multiply by 48 to find out number of interfaces (assuming switch is 48 ports)
num_intefaces = num_switches * 48
print(f"There are total {num_switches} switches and total {num_intefaces}")
print()
```

Another is more advanced example where we will use user input to provide shwo running config of the router. 

```python

