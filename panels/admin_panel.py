from core.user import Employee
from core.data_store import DataStore

class AdminPanel:
    admin_username = "admin"
    admin_password = "1234"

    def login(self):
        print("\n Admin Login")
        username = input("Username: ")
        password = input("Password: ")

        if username == self.admin_username and password == self.admin_password:
            print("Admin logged in successfully!")
            self.menu()
        else:
            print("Invalid username or password!")

    def menu(self):
        while True:
            print("1. Add Employee")
            print("2. Remove Employee")
            print("3. View Employees")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.remove_employee()
            elif choice == "3":
                self.list_employees()
            elif choice == "4":
                break
            else:
                print("Invalid option!")

    def add_employee(self):
        print("Add Employee")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        username = input("Username: ")
        password = input("Password: ")

        for emp in DataStore.employees:
            if emp.username == username:
                print("Username already exists")
                return
            if emp.email == email:
                print("Email already exists")
                return
        
        employee = Employee(username, password, email, first_name, last_name)
        DataStore.employees.append(employee)
        print("Employee added successfully")

    def remove_employee(self):
        print("Remove Employee")
        username = input("Employee username: ")

        for emp in DataStore.employees:
            if emp.username == username:
                DataStore.employees.remove(emp)
                print("Employee removed")
                return
            
        print("Employee not found")

    def list_employees(self):
        print("Employees List")
        if not DataStore.employees:
            print("No employees registered")
            return
        
        for i, emp in enumerate(DataStore.employees, start=1):
            print(f"{i}. {emp.first_name} {emp.last_name} | {emp.username} | {emp.email}")



        





