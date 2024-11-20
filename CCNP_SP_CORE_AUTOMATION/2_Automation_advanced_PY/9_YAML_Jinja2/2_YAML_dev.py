# Python code effectively imports a YAML file and prints its contents as a Python dictionary
# Import the YAML module for parsing YAML files
import yaml

# Define the path to the YAML file containing device information
yaml_file = 'devices.yaml'  # This variable holds the filename of the YAML file

# Open the specified YAML file in read mode
with open(yaml_file, 'r') as file:  # Using 'with' ensures the file is closed after reading
    # Load the contents of the YAML file safely and convert it into a Python dictionary
    devices = yaml.safe_load(file)  # safe_load is used to prevent the execution of any arbitrary code in the YAML

# Print the contents of the devices dictionary to the console
print(devices)  # This will display the parsed data from the YAML file