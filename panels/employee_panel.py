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
                break
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
    
    def add_train(self):
        print("\nAdd train")
        train_name = input("Train name: ")
        if not train_name:
            print("Train name cannot be empty")
            return
        if self.train_exists(train_name):
            print("This train already exists")
            return
        line_name = input("Line name: ")
        if not line_name:
            print("Line name cannot be empty")
            return
        if not self.line_exists(line_name):
            print("This line does not exist")
            return
        speed = int(input("speed: "))
        if not speed:
            print("Speed cannot be empty")
            return
        stoptime = float(input("Stop time: "))
        if not stoptime:
            print("Stop time cannot be empty")
            return
        train_level = int(input("Train level: "))
        if not train_level:
            print("Train level cannot be empty")
            return
        price = int(input("Price: "))
        if not price:
            print("Price cannot be empty")
            return
        capacity = int(input("Capacity: "))
        if not capacity:
            print("Capacity cannot be empty")
            return
        DataStore.trains.append(
            Train(
                train_id=train_name,
                route=line_name,
                average_speed=speed,
                stoppage=stoptime,
                quality_level=train_level,
                price=price,
                capacity=capacity
            )
        )
        print("Train added successfully")
    
    def update_train(self):
        print("\nUpdate train")
        nam = input("Train name: ")
        if not nam:
            print("Train name cannot be empty")
            return
        train = self.get_train(nam)
        if not train:
            print("No train with this name was found")
            return
        print("\n select train information: ")
        print(train)
        print("\nWhich feature do you want to update?")
        print("1. Train name")
        print("2. Line name")
        print("3. Speed")
        print("4. Stop time")
        print("5. Train level")
        print("6. Price")
        print("7. Capacity")

        vizhegi = int(input("choice: "))

        if vizhegi == 1:
            new_name = input("Enter the new train name: ")
            if not new_name or (new_name != train.name and self.train_exists(new_name)):
                print("The new name is invalid or already exists")
                return
            train.name = new_name
            print("Train name is updated successfully")
        elif vizhegi == 2:
            new_line_name = input("Enter the new line name: ")
            if not new_line_name:
                print("Line name cannot be empty")
                return
            train.line_name = new_line_name
            print("Line name is updated successfully")
        elif vizhegi == 3:
            new_speed = int(input("Enter the new speed: "))
            if not new_speed:
                print("Speed cannot be empty")
                return
            train.speed = new_speed
            print("Speed is updated successfully")
        elif vizhegi == 4:
            new_stoptime = float(input("Enter the new stop time: "))
            if not new_stoptime:
                print("Stop time cannot be empty")
                return
            train.stoptime = new_stoptime
            print("Stop time is updated successfully")
        elif vizhegi == 5:
            new_train_level = int(input("Enter the new train level: "))
            if not new_train_level:
                print("Train level cannot be empty")
                return
            train.train_level = new_train_level
            print("Train level is updated successfully")
        elif vizhegi == 6:
            new_price = int(input("Enter the new price: "))
            if not new_price:
                print("Price cannot be empty")
                return
            train.price = new_price
            print("Price is updated successfully")
        elif vizhegi == 7:
            new_capacity = int(input("Enter the new capacity: "))
            if not new_capacity:
                print("Capacity cannot be empty")
                return
            train.capacity = new_capacity
            print("Capacity is updated successfully")
        else:
            print("Invalid option!")
        
    def delete_train(self):
        print("\nDelete train")
        name = input("Enter the name of the train to delete: ")
        if not name:
            print("Train name cannot be empty")
            return
        
        Tr = self.get_train(name)
        if not Tr:
            print("No train with this name was found")
            return

        DataStore.trains.remove(Tr)

        print("the train was successfully deleted")

    def list_trains(self):
        print("\nList of trains")
        if not DataStore.trains:
            print("No trains have been recorded")
            return
        for i, train in enumerate(DataStore.trains, start=1):
            print(f"{i}. {train}")

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
    
    def train_exists (self, name):
        name = name.strip().lower()
        return any(train.name.strip().lower() == name for train in DataStore.trains)

    def get_train(self, name):
        name = name.strip().lower()

        for train in DataStore.trains:
            if train.name.strip().lower() == name:
                return train  
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

    






            




                
                





                











