import sqlite3

conn = sqlite3.connect("cloud.db")
cursor = conn.cursor()

name = input("Enter Name to Search: ")

cursor.execute(
    "SELECT * FROM cloud_data WHERE name LIKE ?",
    ('%' + name + '%',)
)

rows = cursor.fetchall()

if rows:
    print("\nSearch Results")
    print("-" * 75)
    print("{:<5} {:<20} {:<30} {:<15}".format("ID", "NAME", "EMAIL", "PHONE"))

    for row in rows:
        print("{:<5} {:<20} {:<30} {:<15}".format(row[0], row[1], row[2], row[3]))
else:
    print("No Record Found.")

conn.close()

    
