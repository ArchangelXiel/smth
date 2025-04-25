import psycopg2
import csv
import json

conn = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="postgres",
    password="1"
)
cur = conn.cursor()

def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(15)
        )
    """)
    conn.commit()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()

def insert_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            name, phone = row
            cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()

def insert_many_users():
    n = int(input("How many users to insert? "))
    users = []
    for _ in range(n):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        users.append({"name": name, "phone": phone})
    cur.execute("CALL insert_many_users(%s)", (json.dumps(users),))
    cur.execute("FETCH ALL IN \"<unnamed portal 1>\";")
    cur.execute("SELECT * FROM insert_many_users(%s)", (json.dumps(users),))
    result = cur.fetchone()
    print("Incorrect data:", result[0])
    conn.commit()

def update_data():
    name = input("Enter name to update: ")
    phone = input("Enter new phone: ")
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()

def search_pattern():
    pattern = input("Enter pattern to search: ")
    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def get_paginated():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    cur.execute("SELECT * FROM get_paginated_data(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_data():
    val = input("Enter name or phone to delete: ")
    cur.execute("CALL delete_by_name_or_phone(%s)", (val,))
    conn.commit()

def menu():
    create_table()
    while True:
        print("\n1. Insert from console")
        print("2. Insert from CSV")
        print("3. Insert many users")
        print("4. Update user")
        print("5. Search by pattern")
        print("6. Paginate data")
        print("7. Delete user")
        print("8. Exit")
        choice = input("Choose option: ")
        if choice == '1':
            insert_from_console()
        elif choice == '2':
            path = input("Enter CSV path: ")
            insert_from_csv(path)
        elif choice == '3':
            insert_many_users()
        elif choice == '4':
            update_data()
        elif choice == '5':
            search_pattern()
        elif choice == '6':
            get_paginated()
        elif choice == '7':
            delete_data()
        elif choice == '8':
            break
        else:
            print("Invalid option.")

menu()

cur.close()
conn.close()
