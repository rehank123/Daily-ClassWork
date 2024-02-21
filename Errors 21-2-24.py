try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")




try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")





print("https://hackr.io/blog/python-projects#advanced-python-project-ideas")






import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('records.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS records (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    email TEXT
                )''')
conn.commit()

def add_record(name, age, email):
    cursor.execute('''INSERT INTO records (name, age, email) VALUES (?, ?, ?)''', (name, age, email))
    conn.commit()
    print("Record added successfully.")

def view_records():
    cursor.execute('''SELECT * FROM records''')
    records = cursor.fetchall()
    print("ID | Name | Age | Email")
    for record in records:
        print(record)

def remove_record(record_id):
    cursor.execute('''DELETE FROM records WHERE id = ?''', (record_id,))
    conn.commit()
    print("Record removed successfully.")

# Example usage
add_record("Asif Khan", 30, "asif@example.com")
add_record("Waseem zahid", 25, "waseem@example.com")
view_records()
remove_record(1)
view_records()

# Close the connection
conn.close()







# pip install sqlite3
import streamlit as st
import sqlite3

# Function to create a table if it doesn't exist
def create_table():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS records
                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    conn.commit()
    conn.close()

# Function to insert a record into the database
def insert_record(name, age):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''INSERT INTO records (name, age) VALUES (?, ?)''', (name, age))
    conn.commit()
    conn.close()

# Function to display all records
def display_records():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM records''')
    records = c.fetchall()
    conn.close()
    return records

# Function to delete a record from the database
def delete_record(record_id):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''DELETE FROM records WHERE id = ?''', (record_id,))
    conn.commit()
    conn.close()

# Create table if not exists
create_table()

# Streamlit UI
st.title('Record Management App')

# Input fields for record
name = st.text_input('Enter Name')
age = st.number_input('Enter Age')

# Button to add record
if st.button('Add Record'):
    insert_record(name, age)
    st.success('Record Added Successfully!')

# Display all records
st.title('Records')
records = display_records()
for record in records:
    st.write(record)
    if st.button(f'Delete {record[1]}'):
        delete_record(record[0])
        st.success(f'Record ID {record[0]} Deleted Successfully!')


