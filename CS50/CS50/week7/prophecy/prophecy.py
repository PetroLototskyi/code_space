import sqlite3
import csv

# Define the names of the database and CSV file
database_name = "school.db"
csv_file_name = "students.csv"

# Create and connect to the SQLite database
conn = sqlite3.connect(database_name)
cursor = conn.cursor()

# Execute the CREATE TABLE commands from the schema.sql file
with open("schema.sql", "r") as schema_file:
    schema = schema_file.read()
    cursor.executescript(schema)

# Commit the changes to the database
conn.commit()

# Read data from the CSV file and insert it into the database
with open(csv_file_name, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Insert houses into the houses table
        cursor.execute("INSERT OR IGNORE INTO houses (house_name) VALUES (?)", (row["house"],))
        conn.commit()

        # Get the house_id for the student's house
        cursor.execute("SELECT id FROM houses WHERE house_name=?", (row["house"],))
        house_id = cursor.fetchone()[0]

        # Insert students into the students table
        cursor.execute("INSERT INTO students (student_name, house_id, head_id) VALUES (?, ?, ?)",
                       (row["student_name"], house_id, row["head"]))
        conn.commit()

        # Insert house assignments into the house_assignments table
        cursor.execute("INSERT INTO house_assignments (student_id, house_id) VALUES (?, ?)",
                       (cursor.lastrowid, house_id))
        conn.commit()

# Close the database connection
conn.close()

print("Database created and data inserted successfully.")
