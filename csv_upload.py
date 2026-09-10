import sqlite3
import pandas as pd
from validator import validate_data

# Read CSV
data = pd.read_csv("sample.csv")

conn = sqlite3.connect("cloud.db")
cursor = conn.cursor()

for index, row in data.iterrows():

    name = row["name"]
    email = row["email"]
    phone = str(row["phone"])

    result = validate_data(name, email, phone)

    if result == "Unique":
        cursor.execute(
            "INSERT INTO cloud_data(name, email, phone) VALUES (?, ?, ?)",
            (name, email, phone)
        )
        print(f"✅ {name} added.")

    elif result == "Duplicate":
        print(f"❌ {name} is Duplicate.")

    else:
        print(f"⚠️ {name} is False Positive.")

conn.commit()
conn.close()

print("\nCSV Upload Completed.")