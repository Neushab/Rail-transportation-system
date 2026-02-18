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
                print("\nInvalid option!")

    # ---------- Auth ----------

    def employee_login(self): 
        if not DataStore.employees:
            print("\nNo employees have been registered by the admin.")
            return False
        
        while True:
            print("\nEmployee login")
            print("Enter 0 to Exit")
            username = input("Employee username: ")
            if username == "0":
                    print("\nBake to main menu")
                    return False
        
            password = input("Employee password: ")
            if password == "0":
                    print("\nBake to main menu")
                    return False

            for emp in DataStore.employees:
                if emp.username == username and emp.password == password:
                    print("\nEmployee logged in successfully!")
                    return True
                    
            print("\nThe username or password is incorrect")
            continue
    
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
        print("Enter 0 to Exit")

        name = input("line name: ")

        if name == "0":
            print("\nBake to employee menu")
            return
        
        #empty checks (line name)
        if not name:
            print("\nLine name is required")
            return
                
        # uniqueness checks (line name)
        if self.line_exists(name):
            print("\nThis line already exists")
            return
                
        origin = input("origin: ")
        if origin == "0":
            print("\nBake to employee menu")
            return
        
        destination = input("destination: ")
        if destination == "0":
            print("\nBake to employee menu")
            return
        
        #empty checks (origin and destination)
        if not origin or not destination:
            print("\norigin and destination are required")
            return
          
        count_input = input("Number of stations: ")

        if count_input == "0":
            print("\nBack to employee menu")
            return
        
        if not count_input.isdigit():
            print("\nPlease enter a valid number")
            return
        
        count = int(count_input)
        if count < 2:
            print("\nThere should be at least two stations")
            return
        
        stations = []
        for i in range(count):
            s = input(f"station name {i+1}: ")
            if s == "0":
                print("\nBake to employee menu")
                return

            #empty checks (Station)
            if not s:
                print("\nStation name cannot be empty")
                return
            stations.append(s)

        DataStore.lines.append(
            Line(name=name, origin=origin, destination=destination, stations=stations)

        )

        print("\nLine added successfully")                
                

    def update_line(self):
        while True:
            print("\nUpdate line")
            print("Enter 0 to Exit")
        
            name = input("Line name: ")
            if name == "0":
                print("\nBake to employee menu")
                return

            if not name:
                print("\nLine name cannot be empty")
                continue
                
            line = self.get_line(name)
            if not line:
                print("\nNo line with this name was found")
                continue

            while True:    
                print("\nSelected line information: ")
                print(line)

                print("\nWhich feature do you want to update?")
                print("1. line name")
                print("2. origin")
                print("3. destination")
                print("4. List of stations")
                print("5. Exit")

                line_feature_choice = input("choice: ")

                if line_feature_choice == "1":
                    print("Enter 0 to Exit")
                    new_name = input("Enter the new line name: ")
                    if new_name == "0":
                        continue
                    if not new_name or (new_name != line.name and self.line_exists(new_name)):
                        print("\nThe new name is invalid or already exists")
                        continue
                    for t in DataStore.trains:
                        if t.line_name == line.name:
                            t.line_name = new_name
                    line.name = new_name
                    print("\nLine name is updated successfully")

                elif line_feature_choice == "2":
                    print("Enter 0 to Exit")
                    new_origin = input("Enter the new origin: ")
                    if new_origin == "0":
                        continue
                    if not new_origin:
                        print("\nnew origin cannot be empty")
                        continue
                    line.origin = new_origin
                    print("\norigin is updated successfully")

                elif line_feature_choice == "3":
                    print("Enter 0 to Exit")
                    new_destination = input("Enter the new destination: ")
                    if new_destination == "0":
                        continue
                    if not new_destination:
                        print("\nnew destination cannot be empty")
                        continue
                    line.destination = new_destination
                    print("\ndestination is updated successfully")
                    
                elif line_feature_choice == "4":
                    print("\nEnter 0 to Exit")

                    count_input = input("Number of stations: ").strip()
                    if count_input == "0":
                        continue
                    if not count_input.isdigit():
                        print("\nPlease enter a valid number")
                        continue

                    count = int(count_input)
                    if count < 2:
                        print("\nThere should be at least two stations")
                        continue

                    stations = []
                    cancelled = False

                    for i in range(count):
                        s = input(f"Station name {i+1}: ")
                        if s == "0":
                            cancelled = True
                            break
                        
                        if not s:
                            print("\nStation name cannot be empty")
                            cancelled = True
                            break
                        stations.append(s)

                    if cancelled:
                        continue

                    line.stations = stations

                    print("\nThe station list has been updated")

                elif line_feature_choice == "5":
                    print("\nBake to employee menu")
                    return

                else:
                    print("\nInvalid option!")


    def delete_line(self):
        while True:
            print("\nDelete Line")
            print("Enter 0 to Exit")
            name = input("Line name: ")
            if name == "0":
                print("\nBake to employee menu")
                return 
            
            if not name:
                print("\nLine name cannot be empty")
                continue
                    
            line = self.get_line(name)
            if not line:
                print("\nNo line with this name was found")
                continue
                
            DataStore.lines.remove(line)
            DataStore.trains = [t for t in DataStore.trains if t.line_name != name]

            print("\nThe line was successfully deleted")
            return


    def list_lines(self):
        print("\nList of lines")

        if not DataStore.lines:
            print("\nNo lines have been recorded")
            return
                
        for i, line in enumerate(DataStore.lines, start=1):
            print(f"{i}. {line}")

    # ---------- Train ----------
    
    def add_train(self):
        print("\nAdd train")
        print("Enter 0 to Exit")
        
        train_name = input("Train ID: ")

        if train_name == "0":
            print("\nBake to employee menu")
            return
        
        if not train_name:
            print("Train name cannot be empty")
            return
        
        if self.train_exists(train_name):
            print("This train already exists")
            return
        
        line_name = input("Line name: ")

        if line_name == "0":
            print("\nBake to employee menu")
            return
        
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
        train_id = input("Train ID: ")
        if not train_id:
            print("Train ID cannot be empty")
            return
        train = self.get_train(train_id)
        if not train:
            print("No train with this ID was found")
            return
        print("\n select train information: ")
        print(train)
        print("\nWhich feature do you want to update?")
        print("1. Train ID")
        print("2. Route (Line name)")
        print("3. Average speed")
        print("4. Stoppage (Stop time)")
        print("5. Quality level (Train level)")
        print("6. Price")
        print("7. Capacity")

        vizhegi = int(input("choice: "))

        if vizhegi == 1:
            new_train_id = input("Enter the new Train ID: ")
            if not new_train_id or (new_train_id != train.train_id and self.train_exists(new_train_id)):
                print("The new Train ID is invalid or already exists")
                return
            train.train_id = new_train_id
            print("Train ID is updated successfully")
        elif vizhegi == 2:
            new_route = input("Enter the new route (Line name): ")
            if not new_route:
                print("Route cannot be empty")
                return
            train.route = new_route
            print("Route is updated successfully")
        elif vizhegi == 3:
            new_speed = int(input("Enter the new average speed: "))
            if not new_speed:
                print("Average speed cannot be empty")
                return
            train.average_speed = new_speed
            print("Average speed is updated successfully")
        elif vizhegi == 4:
            new_stoppage = float(input("Enter the new stoppage (stop time): "))
            if not new_stoppage:
                print("Stoppage cannot be empty")
                return
            train.stoppage = new_stoppage
            print("Stoppage is updated successfully")
        elif vizhegi == 5:
            new_quality_level = int(input("Enter the new quality level (train level): "))
            if not new_quality_level:
                print("Quality level cannot be empty")
                return
            train.quality_level = new_quality_level
            print("Quality level is updated successfully")
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

    @staticmethod
    def get_train(train_id):

        for t in DataStore.trains:
            if t.train_id.strip().lower() == train_id.lower:
                return t  
        return None                      


    






            




                
                





                











