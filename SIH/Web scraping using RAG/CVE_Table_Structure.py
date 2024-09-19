# Ensure the table element exists
if table is None:
    print("Table not found. Check the structure or class name.")
else:
    # Try finding all rows inside the table without specifying a class
    rows = table.find_all('tr')
    print(f"Number of rows found: {len(rows)}")  # This should return a number greater than 0
