# Checking Built-in Attributes and Methods of a Variable in Python

In Python, we can check the built-in attributes and methods associated with a specific variable using the `dir()` command.
Below is an example that demonstrates this with the integer variable `num`.

## Example

```python
num = 20
print(dir(num))
```

### Output

When you run the above code, the output will be as follows:

```
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', 
 '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', 
 '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', 
 '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', 
 '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', 
 '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', 
 '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', 
 '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', 
 '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 
 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 
 'numerator', 'real', 'to_bytes']
```

### Explanation

Using the `dir()` function, you can explore the capabilities of different variable types in Python, making it a valuable tool for developers.

