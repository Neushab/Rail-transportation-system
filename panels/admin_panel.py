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
                print("\nInvalid option!")

    # ---------- Auth ----------

    def admin_login(self) -> bool:
        while True:
            print("Enter 0 to Exit")
            username = input("Username: ")
            if username == "0":
                print("\nBake to main menu")
                return False
            password = input("Password: ")
            if password == "0":
                print("\nBake to main menu")
                return False
            if username == admin_username and password == admin_password:
                print("\nAdmin logged in successfully!")
                return True
            print("\nInvalid username or password!")
            continue

    # ---------- Menu ----------

    @staticmethod
    def admin_menu():
        print("\nAdmin Menu:")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. View Employees")
        print("4. Exit")

    def add_employee(self):
        while True:
            print("\nAdd Employee")
            print("Enter 0 to Exit")
            first_name = input("First name: ")
            if first_name == "0":
                print("\nBake to admin menu")
                return 
            last_name = input("Last name: ")
            if last_name == "0":
                print("\nBake to admin menu")
                return 
            email = input("Email: ")
            if email == "0":
                print("\nBake to admin menu")
                return 
            username = input("Username: ")
            if username == "0":
                print("\nBake to admin menu")
                return 
            password = input("Password: ")
            if password == "0":
                print("\nBake to admin menu")
                return 

            #empty checks
            if not all([first_name, last_name, email, username, password]):
                print("\nAll fields are required.")
                continue
            
            # validations
            if not validate_email(email):
                print("\nEmail format is invalid.")
                continue
            
            if not validate_password(password):
                print("\nThe password must contain English letters + numbers + @ or &")
                continue
            
            # uniqueness checks
            if self.email_exists(email):
                print("\nThis email already exists")
                continue
            
            if self.username_exists(username):
                print("\nThis username already exists")
                continue
            
            employee = Employee(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )

            DataStore.employees.append(employee)
            print("\nEmployee added successfully")
            return

    def remove_employee(self):
        while True:
            print("\nRemove Employee")
            print("Enter 0 to Exit")
            username = input("Employee username: ")
            if username == "0":
                print("\nBake to admin menu")
                return 
            if not username:
                print("\nUsername cannot be empty")
                continue
            
            for emp in DataStore.employees:
                if emp.username == username:
                    DataStore.employees.remove(emp)
                    print("\nEmployee removed")
                    return
                
            print("\nNo employee with this username was found")
            continue

    def list_employees(self):
        print("\nList of employees")
        if not DataStore.employees:
            print("\nNo employees registered")
            return
        
        for i, emp in enumerate(DataStore.employees, start=1):
            print(f"{i}. {emp}")

    @staticmethod
    def email_exists(email: str) -> bool:
        return any(emp.email.lower() == email.lower() for emp in DataStore.employees)
    
    @staticmethod
    def username_exists(username: str) -> bool:
        return any(emp.username.lower() == username.lower() for emp in DataStore.employees)





        





