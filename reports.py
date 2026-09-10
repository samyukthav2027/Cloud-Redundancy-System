import sqlite3

conn = sqlite3.connect("cloud.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM cloud_data")
total = cursor.fetchone()[0]

print("\n===== DATABASE REPORT =====")
print("Total Unique Records:", total)

conn.close()
