from core.data_store import DataStore
from core.railway import Line, Train

class EmployeePanel:
    def run(self):
        print("\nEmployee Panel")

        if not self.employee_login():
            return
        
        while True:
            self.employee_menu()
            choice = input("Choose an option: ")

            if choice == "1":
                self.add_line()
            elif choice == "2":
                self.update_line()
            elif choice == "3":
                self.delete_line()
            elif choice == "4":
                self.list_lines()
            elif choice == "5":
                self.add_train()
            elif choice == "6":
                self.update_train()
            elif choice == "7":
                self.delete_train()
            elif choice == "8":
                self.list_trains()
            elif choice == "9":
                print("\nBack to main menu")
            else:
                print("Invalid option!")

            # ---------- Auth ----------

            def employee_login(self):
                if not DataStore.employees:
                    print("No employees have been registered by the admin.")
                    return False
                
                username = input("Employee username: ")
                password = input("Employee password: ")

                for emp in DataStore.employees:
                    if emp.username == username and emp.password == password:
                        print("Employee logged in successfully!")
                        return True
                    
                print("The username or password is incorrect")

            # ---------- Menu ----------

            @staticmethod
            def employee_menu():
                print("\nEmployee Menu:")
                print("1. Add line")
                print("2. Update line")
                print("3. Delete line")
                print("4. Show lines")
                print("5. Add train")
                print("6. Update train")
                print("7. Delete train")
                print("8. Show trains")
                print("9. Exit")

            # ---------- Line ----------

            def add_line(self):
                print("\nAdd line")
                name = input("line name: ")
                origin = input("origin: ")
                destination = input("destination: ")
                _count = input("line count: ")
                stations = input("list of station names: ")

                #empty checks
                if not all([name, origin, destination, _count, stations]):
                    print("All fields are required.")
                    return
                
                if self.line_exists(name):
                    print("This line already exists")
                    return
                
                line = Line(
                    name = name,
                    origin = origin,
                    destination = destination,
                    _count = _count,
                    stations = stations
                )

                DataStore.lines.append(line)
                print("Line added successfully")
                

            def update_line(self):
                print("\nUpdate line")


            def list_lines(self):
                print("Show lines")
                if not DataStore.lines:
                    print("No lines have been recorded")
                    return
                
                for i, line in enumerate(DataStore.lines, start=1):
                    print(f"{i}. {line.name} | {line.origin} -> {line.destination} | {line._count} | {line.stations}")




                
                





                











