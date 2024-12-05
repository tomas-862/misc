
# SQLite Usage Guide

## Displaying Query Results in Table Format

To present your SQL query results in a clear, tabular format, follow these steps:

1. **Open SQLite**: Launch your SQLite database by using the following command in your terminal:
   ```bash
   sqlite3
   ```

2. **Set the Output Mode to Table**: This command configures SQLite to display results in a table format:
   ```bash
   .mode table
   ```

## Creating a Permanent Configuration File

You can create a configuration file to set default preferences for your SQLite sessions. This file, named `.sqliterc`, is read automatically on startup.

### Steps to Create/Modify the .sqliterc File:

1. **Locate Your Home Directory**:
   - **Linux/WSL**: Typically located at `~/` (e.g., `/home/username/`).
   - **Windows**: Usually found at `C:\Users\YourUsername`.

2. **Open or Create the .sqliterc File**: Use a text editor to create or edit the `.sqliterc` file in your home directory. For example, with the `nano` editor:
   ```bash
   nano ~/.sqliterc
   ```

3. **Add Your Preferred Settings**: Include the following commands in your `.sqliterc` file to set the default output mode and enable headers for better readability:
   ```sql
   -- Set output mode to table
   .mode table

   -- Enable headers
   .headers on
   ```

## Executing SQL Files in SQLite

To run a SQL file (.sql) and execute the queries contained within it, follow these steps:

1. **Open the SQLite Database**: Begin by opening your SQLite database:
   ```bash
   sqlite3 songs.db
   ```

2. **Execute the SQL File**: While inside the SQLite shell, use the `.read` command to execute your SQL file:
   ```bash
   .read 1.sql
   ```