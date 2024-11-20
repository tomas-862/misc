
# code for generating an iBGP configuration using Jinja2 template 

from jinja2 import Template  # Import the Template class from the jinja2 library for template rendering

# Define the Jinja2 template for iBGP configuration
ibgp_template = Template("""
router bgp {{ local_as }}
    {% for neighbor in neighbors %}
     neighbor {{ neighbor.ip }} remote-as {{ local_as }}
      {% if neighbor.description %}
        description {{ neighbor.description }}
      {% endif %}
    {% endfor %}
""")

# Prepare the BGP configuration using the render method of the template
bgp_config = ibgp_template.render(
    local_as=65000,  # Pass the local AS number to the template
    neighbors=[  # Provide a list of neighbors, each with an IP and an optional description
        {'ip': '192.168.1.1', 'description': 'Router1 in same AS'},  # First neighbor configuration
        {'ip': '192.168.1.2', 'description': 'Router2 in same AS'}  # Second neighbor configuration
    ]
)

# Output the generated BGP configuration to the console
print(bgp_config)  # Print the final configuration created from the template
