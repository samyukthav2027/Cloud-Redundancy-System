import sqlite3
import re
from fuzzywuzzy import fuzz

def validate_data(name, email, phone):

    if not re.match(r'^[A-Za-z ]+$', name):
        return "Invalid Name"

    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return "Invalid Email"

    if not re.match(r'^\d{10}$', phone):
        return "Invalid Phone"

    conn = sqlite3.connect("cloud.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name,email,phone FROM cloud_data")
    rows = cursor.fetchall()

    conn.close()

    for row in rows:

        if email == row[1]:
            return "Duplicate"

        if phone == row[2]:
            return "Duplicate"

        similarity = fuzz.ratio(name.lower(), row[0].lower())

        if similarity >= 85:
            return "False Positive"

    return "Unique"