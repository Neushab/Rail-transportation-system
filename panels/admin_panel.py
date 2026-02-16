from core.user import Employee
from core.data_store import DataStore
from core.validators import validate_email, validate_password


admin_username = "admin"
admin_password = "1234"


class AdminPanel:
    def run(self):
        print("\nAdmin Login")
        if not self.admin_login():
            return
        
        while True:
            self.admin_menu()
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.remove_employee()
            elif choice == "3":
                self.list_employees()
            elif choice == "4":
                print("\nBack to main menu")
                return
            else:
                print("Invalid option!")

    # ---------- Auth ----------

    def admin_login(self) -> bool:
        username = input("Username: ")
        password = input("Password: ")
        if username == admin_username and password == admin_password:
            print("Admin logged in successfully!")
            return True
        print("Invalid username or password!")

    # ---------- Menu ----------

    @staticmethod
    def admin_menu():
        print("\nAdmin Menu:")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. View Employees")
        print("4. Exit")

    def add_employee(self):
        print("\nAdd Employee")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        username = input("Username: ")
        password = input("Password: ")

        #empty checks
        if not all([first_name, last_name, email, username, password]):
            print("\nAll fields are required.")
            return
        
        # validations
        if not validate_email(email):
            print("\nEmail format is invalid.")
            return
        
        if not validate_password(password):
            print("\nThe password must contain English letters + numbers + @ or &")
            return
        
        # uniqueness checks
        if self.email_exists(email):
            print("\nThis email already exists")
            return
        
        if self.username_exists(username):
            print("\nThis username already exists")
            return
        
        employee = Employee(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
        )

        DataStore.employees.append(employee)
        print("\nEmployee added successfully")

    def remove_employee(self):
        print("\nRemove Employee")
        username = input("Employee username: ")
        if not username:
            print("\nUsername cannot be empty")
            return
        
        for emp in DataStore.employees:
            if emp.username == username:
                DataStore.employees.remove(emp)
                print("\nEmployee removed")
                return
            
        print("\nNo employee with this username was found")

    def list_employees(self):
        print("\nList of employees")
        if not DataStore.employees:
            print("No employees registered")
            return
        
        for i, emp in enumerate(DataStore.employees, start=1):
            print(f"{i}. {emp.first_name} {emp.last_name} | {emp.username} | {emp.email}")

    @staticmethod
    def email_exists(email: str) -> bool:
        return any(emp.email.lower() == email.lower() for emp in DataStore.employees)
    
    @staticmethod
    def username_exists(username: str) -> bool:
        return any(emp.username.lower() == username.lower() for emp in DataStore.employees)





        





