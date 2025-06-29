import csv
import datetime

# Input CSV filename
INPUT_CSV = 'rules_to_decommission.csv'
# Output TXT filename with CLI commands
OUTPUT_TXT = 'firewall_commands.txt'

# Read the CSV file
with open(INPUT_CSV, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rules = [row for row in reader]

# Get current date for description
current_date = datetime.date.today().strftime('%d-%m-%Y')

commands = []

for rule in rules:
    vsys = rule['vsys'].strip()
    rule_name = rule['rule_name'].strip()
    change_name = rule['change_name'].strip()
    implementer = rule['implementer'].strip()

    description = f"Change: {change_name}\nDate: {current_date}\nImplementer: {implementer}"

    # Commands
    # 1. Add tag - assuming using the 'tag' command if available (or skip if not)
    # For simplicity, assuming tags are added via 'set rule ... tag ...'
    # Note: Actual syntax depends on the device's CLI syntax

    # Example: Add tag (may need adjustment)
    cmd_add_tag = f"set rulebase security rules \"{rule_name}\" tag \"{change_name}\""
    commands.append(f"# Vsys: {vsys}, Rule: {rule_name}")
    commands.append(cmd_add_tag)

    # 2. Update description
    cmd_update_desc = f"set rulebase security rules \"{rule_name}\" description \"{description}\""
    commands.append(cmd_update_desc)

    # 3. Disable the rule
    cmd_disable = f"set rulebase security rules \"{rule_name}\" disable yes"
    commands.append(cmd_disable)

    # 4. Move rule to bottom
    # There is no direct CLI command for 'move to bottom', but one way is to delete and re-add at bottom
    # Or use 'move' command if available
    # Example (assuming move command):
    # move command placeholder
    cmd_move_bottom = f"move rulebase security rules \"{rule_name}\" bottom"
    commands.append(cmd_move_bottom)

    commands.append('')  # blank line for readability

# Write all commands to output file
with open(OUTPUT_TXT, 'w') as outfile:
    for line in commands:
        outfile.write(line + '\n')

print(f"CLI commands have been written to {OUTPUT_TXT}")