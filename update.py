import sqlite3

id = input("Enter ID to Update: ")
new_email = input("Enter New Email: ")
new_phone = input("Enter New Phone: ")

conn = sqlite3.connect("cloud.db")
cursor = conn.cursor()

cursor.execute(
    "UPDATE cloud_data SET email=?, phone=? WHERE id=?",
    (new_email, new_phone, id)
)

conn.commit()

if cursor.rowcount > 0:
    print("Record Updated Successfully.")
else:
    print("Record Not Found.")

conn.close()