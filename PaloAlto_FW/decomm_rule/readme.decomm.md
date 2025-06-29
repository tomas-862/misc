Palo Alto Panorama Rule Decommissioning Script
This Python script helps automate the process of decommissioning security rules in Palo Alto Panorama by generating CLI commands based on an Excel input file. The script reads rule details from an Excel sheet, prepares the necessary CLI commands, and writes them to a text file for easy execution.
Features

Input Excel File: Reads rule details from an Excel file (rules_to_decommission.xlsx).
CLI Commands: Generates CLI commands for:
Adding a tag to the rule.
Updating the rule description.
Disabling the rule.
Moving the rule to the bottom of the rulebase.
Output File: Writes the generated CLI commands to a text file (firewall_commands.txt).
Prerequisites

Python 3.x
openpyxl library (install via pip install openpyxl)
Usage

Prepare the Input Excel File:
Create an Excel file named rules_to_decommission.xlsx with the following columns:
vsys: The VSYS (Virtual System) where the rule resides.
rule_name: The name of the rule to be decommissioned.
change_name: The change name or identifier.
implementer: The name of the person implementing the change.
Ensure the first row contains the headers as shown above.
Run the Script:
Execute the script using Python:
bash
Copy
python decommission_rules.py
Output:
The script will generate a text file named firewall_commands.txt containing the CLI commands.
Execute these commands in Palo Alto Panorama to decommission the rules.
Example Input Excel File

vsys	rule_name	change_name	implementer
vsys1	Rule1	Change123	John Doe
vsys2	Rule2	Change456	Jane Smith
Example Output CLI Commands

plaintext
Copy
set device-group vsys1 post-rulebase security rules Rule1 tag Change123_decomm
set device-group vsys1 post-rulebase security rules Rule1 description "Change123 / 29.06.2025 John Doe"
set device-group vsys1 post-rulebase security rules Rule1 disable yes
move device-group vsys1 rulebase security rules Rule1 bottom

set device-group vsys2 post-rulebase security rules Rule2 tag Change456_decomm
set device-group vsys2 post-rulebase security rules Rule2 description "Change456 / 29.06.2025 Jane Smith"
set device-group vsys2 post-rulebase security rules Rule2 disable yes
move device-group vsys2 rulebase security rules Rule2 bottom
Customization

Input File Name: Modify the INPUT_EXCEL variable in the script to use a different Excel file.
Output File Name: Modify the OUTPUT_TXT variable to change the output file name.
Sheet Selection: If your Excel file has multiple sheets, modify the wb.active line to select the appropriate sheet.
Notes

The script skips rules with an empty rule_name.
If change_name or implementer is missing, default values (NoChange and Unknown) are used.
The script uses the current date in dd.mm.YYYY format for the rule description.
License

This script is provided as-is, without any warranty. Feel free to modify and distribute it as needed.
