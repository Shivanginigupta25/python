# ---------------------- STUDENT MANAGEMENT SYSTEM ----------------------

students = []  # List to store student data

# ------------ FUNCTION TO VERIFY MOBILE NUMBER -------------
def verify_mobile(mobile):
    return len(mobile) == 10 and mobile.isdigit() and mobile.startswith("9")

# ------------ LOGIN SYSTEM BASED ON ROLE --------------------
def login():
    print("------ Login System ------")
    mobile = input("Enter Mobile Number: ")

    if not verify_mobile(mobile):
        print("Invalid Mobile Number! Must be 10 digits & start with 9.")
        return None

    print("\nSelect User Type:")
    print("1. Admin User")
    print("2. Normal User")
    print("3. Guest User")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        return "admin"
    elif choice == "2":
        return "normal"
    elif choice == "3":
        return "guest"
    else:
        print("Invalid choice!")
        return None

# ------------ MENU FUNCTIONS BASED ON PRIVILEGE -------------

def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll No: ")
    students.append({"name": name, "roll": roll})
    print("Student Added Successfully!")

def delete_student():
    roll = input("Enter Roll No to Delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student Deleted!")
            return
    print("No Student Found!")

def view_students():
    print("\n---- Student List ----")
    if not students:
        print("No Data Available!")
    else:
        for s in students:
            print("Name:", s["name"], "| Roll:", s["roll"])

def search_student():
    roll = input("Enter Roll No to Search: ")
    for s in students:
        if s["roll"] == roll:
            print("Student Found -> Name:", s["name"])
            return
    print("Student Not Found!")

# ------------ DISPLAY MENUS BASED ON ROLE -------------

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. View Student List")
        print("4. Search Student")
        print("5. Logout")
        choice = input("Enter Option: ")

        if choice == "1": add_student()
        elif choice == "2": delete_student()
        elif choice == "3": view_students()
        elif choice == "4": search_student()
        elif choice == "5": break
        else: print("Invalid Input!")

def normal_menu():
    while True:
        print("\n--- Normal User Menu ---")
        print("1. View Student List")
        print("2. Search Student")
        print("3. Logout")
        choice = input("Enter Option: ")

        if choice == "1": view_students()
        elif choice == "2": search_student()
        elif choice == "3": break
        else: print("Invalid Input!")

def guest_menu():
    while True:
        print("\n--- Guest User Menu ---")
        print("1. View Student List")
        print("2. Logout")
        choice = input("Enter Option: ")

        if choice == "1": view_students()
        elif choice == "2": break
        else: print("Invalid Input!")


# ---------------------- MAIN AREA -----------------------

role = login()

if role == "admin":
    admin_menu()
elif role == "normal":
    normal_menu()
elif role == "guest":
    guest_menu()
else:
    print("Login Failed!")
