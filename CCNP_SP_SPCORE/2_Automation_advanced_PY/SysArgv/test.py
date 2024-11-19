import sys

# Check if the user provided an argument
if len(sys.argv) < 2:
    print("No command provided. Please provide a command.")
    sys.exit(1)

# Get the command from the command-line arguments
command = sys.argv[1]

# Strip quotes from the command
command = command.strip().strip('"').strip("'")

# Show the stripped command
print(f"Command without quotes: {command}")


