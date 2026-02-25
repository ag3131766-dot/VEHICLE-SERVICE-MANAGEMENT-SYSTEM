import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Add your MySQL password if needed
    database="vehicle_service_db"
)

cursor = conn.cursor()
def login():
    print("\n---- LOGIN ----")
    username = input("Username: ")
    password = input("Password: ")

    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        print("Login Successful!\n")
        return True
    else:
        print("Invalid Login!\n")
        return False
def add_customer():
    print("\n--- Add Customer ---")
    name = input("Name: ")
    phone = input("Phone: ")
    address = input("Address: ")

    query = "INSERT INTO customers (name, phone, address) VALUES (%s,%s,%s)"
    cursor.execute(query, (name, phone, address))
    conn.commit()
    print("Customer Added Successfully!\n")

def view_customers():
    print("\n--- Customer List ---")
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()

    for row in rows:
        print("ID:", row[0], "| Name:", row[1], "| Phone:", row[2], "| Address:", row[3])
    print()

def add_vehicle():
    print("\n--- Add Vehicle ---")
    customer_id = input("Customer ID: ")
    vehicle_no = input("Vehicle Number: ")
    model = input("Model: ")

    query = "INSERT INTO vehicles (customer_id, vehicle_no, model) VALUES (%s,%s,%s)"
    cursor.execute(query, (customer_id, vehicle_no, model))
    conn.commit()
    print("Vehicle Added Successfully!\n")

def create_service():
    print("\n--- Create Service ---")
    vehicle_id = input("Vehicle ID: ")
    service_charge = float(input("Service Charge: "))
    parts_cost = float(input("Spare Parts Cost: "))

    subtotal = service_charge + parts_cost
    tax = subtotal * 0.18
    total = subtotal + tax

    query = """INSERT INTO services 
               (vehicle_id, service_charge, parts_cost, total_amount)
               VALUES (%s,%s,%s,%s)"""
    cursor.execute(query, (vehicle_id, service_charge, parts_cost, total))
    conn.commit()

    print("\n------ INVOICE ------")
    print("Service Charge:", service_charge)
    print("Parts Cost:", parts_cost)
    print("Tax (18%):", tax)
    print("Total Amount:", total)
    print("---------------------\n")

def menu():
    while True:
        print("====== VEHICLE SERVICE MANAGEMENT SYSTEM ======")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Add Vehicle")
        print("4. Create Service & Generate Bill")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            add_vehicle()
        elif choice == "4":
            create_service()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid Choice!\n")

if login():
    menu()

conn.close()