from core.data_store import DataStore
from core.user import Employee
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
        return False
    

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

        #empty checks (line name)
        if not name:
            print("Line name is required")
            return
                
        # uniqueness checks (line name)
        if self.line_exists(name):
            print("This line already exists")
            return
                
        origin = input("origin: ")
        destination = input("destination: ")

        #empty checks (origin and destination)
        if not origin or not destination:
            print("origin and destination are required")
            return
                
        count = self.read_int("Number of stations: ")
        if count is None or count <= 0:
            print("There should be at least one station")
            return
                
        stations = []
        for i in range(count):
            s = input(f"station name {i+1}: ")

            #empty checks (Station)
            if not s:
                print("Station name cannot be empty")
                return
            stations.append(s)

        DataStore.lines.append(
            Line(name=name, origin=origin, destination=destination, stations=stations)

        )

        print("Line added successfully")                
                

    def update_line(self):
        print("\nUpdate line")
        name = input("Line name: ")
        if not name:
            print("Line name cannot be empty")
            return
                
        line = self.get_line(name)
        if not line:
            print("No line with this name was found")
            return
                
        print("\nSelected line information: ")
        print(line)

        print("\nWhich feature do you want to update?")
        print("1. line name")
        print("2. origin")
        print("3. destination")
        print("4. List of stations")

        line_feature_choice = input("choice: ")

        if line_feature_choice == "1":
            new_name = input("Enter the new line name: ")
            if not new_name or (new_name != line.name and self.line_exists(new_name)):
                print("The new name is invalid or already exists")
                return
            for t in DataStore.trains:
                if t.line_name == line.name:
                    t.line_name = new_name
            line.name = new_name
            print("Line name is updated successfully")

        elif line_feature_choice == "2":
            new_origin = input("Enter the new origin: ")
            if not new_origin:
                print("new origin cannot be empty")
                return
            line.origin = new_origin
            print("origin is updated successfully")

        elif line_feature_choice == "3":
            new_destination = input("Enter the new destination: ")
            if not new_destination:
                print("new destination cannot be empty")
                return
            line.destination = new_destination
            print("destination is updated successfully")
                
        elif line_feature_choice == "4":
            count = self.read_int("Number of stations: ")
            if count is None or count <= 0:
                print("The number is invalid")
                return
            stations = []
            for i in range(count):
                s = input(f"Station name {i+1}: ")
                if not s:
                    print("Station name cannot be empty")
                    return
                stations.append(s)
                line.stations = stations
                print("The station list has been updated")

        else:
            print("Invalid option!")

    def delete_line(self):
        print("Delete Line")
        name = input("Line name: ")
        if not name:
            print("Line name cannot be empty")
            return
                
        line = self.get_line(name)
        if not line:
            print("No line with this name was found")
            return
                
        DataStore.lines.remove(line)
        DataStore.trains = [t for t in DataStore.trains if t.line_name != name]

        print("The line was successfully deleted")

    def list_lines(self):
        print("List of lines")

        if not DataStore.lines:
            print("No lines have been recorded")
            return
                
        for i, line in enumerate(DataStore.lines, start=1):
            print(f"{i}. {line}")

    # ---------- Train ----------


    # ---------- Helpers ----------

    def line_exists (self, name):
        name = name.strip().lower()
        return any(line.name.strip().lower() == name for line in DataStore.lines)
            
    def get_line(self, name):
        name = name.strip().lower()

        for line in DataStore.lines:
            if line.name.strip().lower() == name:
                return line
            
        return None
                
    @staticmethod
    def safe_int(value):
        try:
            return int(value)
        except ValueError:
            return None
                
    def read_int(self, prompt):
        _input = input(prompt).strip()
        if not _input:
            return None
        return self.safe_int(_input)

                






            




                
                





                











