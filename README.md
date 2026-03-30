# list of employee
listt = []
def add_employee():
    while True:
        name = input("Enter name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        # checking email
        for emp in listt:
            if emp[2] == email:
                print("This email already exists!")
                return
        # checking username
        for emp in listt:
            if emp[3] == username:
                print("This username already exists!")
                return
        employee = [name, last_name, email, username, password]
        listt.append(employee)

        print("Employee added successfully!")
        break
def del_employee():
    username = input("Enter the username: ")
    found = False
    for emp in listt:
        if emp[3] == username:
            listt.remove(emp)
            found = True
            print("Employee deleted successfully!")
            break
    if not found:
        print("Username does not exist!")
def view_employee():
    if not listt:
        print("No employees found.")
        return
    print("\nEmployees list:")
    for emp in listt:
        print(emp)
    
while True:
    print("1. Add employee")
    print("2. Delete employee")
    print("3. View employees")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            add_employee()
        case 2:
            del_employee()
        case 3:
            view_employee()
        case 4:
            print("Goodbye!")
            break
        case _:
            print("Invalid choice!")
