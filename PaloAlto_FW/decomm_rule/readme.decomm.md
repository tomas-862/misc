# Palo Alto Panorama Rule Decommissioning Script

This Python script automates the process of decommissioning security rules in Palo Alto Panorama by generating CLI commands based on an Excel input file. The script reads rule details from an Excel sheet, prepares the necessary CLI commands, and writes them to a text file for easy execution.

## Features

- **Input Excel File**: Reads rule details from an Excel file (`rules_to_decommission.xlsx`).
- **CLI Commands**: Generates CLI commands for:
  - Adding a tag to the rule.
  - Updating the rule description.
  - Disabling the rule.
  - Moving the rule to the bottom of the rulebase.
- **Output File**: Writes the generated CLI commands to a text file (`firewall_commands.txt`).

## Prerequisites

- **Python 3.x**
- **openpyxl library** (install via `pip install openpyxl`)

## Usage

### 1. Prepare the Input Excel File:
Create an Excel file named `rules_to_decommission.xlsx` with the following columns:
- `vsys`: The VSYS (Virtual System) where the rule resides.
- `rule_name`: The name of the rule to be decommissioned.
- `change_name`: The change name or identifier.
- `implementer`: The name of the person implementing the change.

Ensure the first row contains the headers as shown above.

### 2. Run the Script:
Execute the script using Python:

```bash
python decommission_rules.py
