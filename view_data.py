import sqlite3

conn = sqlite3.connect("cloud.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM cloud_data")
rows = cursor.fetchall()

if len(rows) == 0:
    print("No records found.")
else:
    print("\n------ CLOUD DATABASE ------")
    print("{:<5} {:<20} {:<30} {:<15}".format("ID", "NAME", "EMAIL", "PHONE"))
    print("-" * 75)

    for row in rows:
        print("{:<5} {:<20} {:<30} {:<15}".format(row[0], row[1], row[2], row[3]))

conn.close()