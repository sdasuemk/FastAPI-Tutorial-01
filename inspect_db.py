import sqlite3

def print_table(cursor, table_name):
    print(f"\n--- Table: {table_name} ---")
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    if not rows:
        print("(Empty)")
        return

    # Get column names
    names = [description[0] for description in cursor.description]
    header = " | ".join(names)
    print(header)
    print("-" * len(header))
    
    for row in rows:
        print(" | ".join(map(str, row)))

try:
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()

    # Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if not tables:
        print("No tables found in database.")
    else:
        for table in tables:
            print_table(cursor, table[0])

except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    if conn:
        conn.close()
