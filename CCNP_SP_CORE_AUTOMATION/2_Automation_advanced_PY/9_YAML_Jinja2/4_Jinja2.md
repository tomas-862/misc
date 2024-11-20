## Jinja2

- **Jinja2** is a modern templating language for Python that facilitates the generation of dynamic content.
- It is widely recognized as the industry standard for templating in Python applications.
- Jinja2 is easy to use and integrates seamlessly with Python code.

### Examples of Jinja2

1. **Creating a BGP Configuration Script with Python Using a Jinja2 Template** 
   - This example demonstrates how to generate an iBGP configuration using a Jinja2 template. Note that Jinja2 templates can be created as separate files, but in this case, we will define the template directly in the script.

```python
from jinja2 import Template  # Import the Template class from the jinja2 library for template rendering

# Define the Jinja2 template for iBGP configuration
ibgp_template = Template("""
router bgp {{ local_as }}  # Declare the router BGP configuration using the local AS number
    {% for neighbor in neighbors %}  # Loop through each neighbor in the neighbors list
     neighbor {{ neighbor.ip }} remote-as {{ local_as }}  # Set the remote AS for the current neighbor
      {% if neighbor.description %}  # Check if the neighbor has a description
        description {{ neighbor.description }}  # Add the neighbor's description if it exists
      {% endif %}  # End of the if statement for checking neighbor description
    {% endfor %}  # End of the loop that processes all neighbors
""")

# Prepare the BGP configuration using the render method of the template
bgp_config = ibgp_template.render(
    local_as=65000,  # Pass the local AS number to the template
    neighbors=[  # Provide a list of neighbors for the BGP configuration
        {'ip': '192.168.1.1', 'description': 'Router1 in same AS'},  # Configuration for first neighbor
        {'ip': '192.168.1.2', 'description': 'Router2 in same AS'}  # Configuration for second neighbor
    ]
)

# Output the generated BGP configuration to the console
print(bgp_config)  # Print the final configuration created from the template

# Output:
# > python .\5_Jinja2.py
#
# router bgp 65000
#
#     neighbor 192.168.1.1 remote-as 65000
#
#        description Router1 in same AS
#
#
#     neighbor 192.168.1.2 remote-as 65000
#
#        description Router2 in same AS
#
#> 
```



