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
        while True:
            print("\nAdd line")
            print("Enter 0 to Exit")

            name = input("line name: ")

            if name == "0":
                print("\nBake to employee menu")
                return
            
            #empty checks (line name)
            if not name:
                print("\nLine name is required")
                continue
                    
            # uniqueness checks (line name)
            if self.line_exists(name):
                print("\nThis line already exists")
                continue
                    
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
                continue
            
            if origin == destination:
                print("\norigin and destination cannot be the same")
                continue
            
            count_input = input("Number of stations: ")

            if count_input == "0":
                print("\nBack to employee menu")
                return
            
            if not count_input.isdigit():
                print("\nPlease enter a valid number")
                continue
            
            count = int(count_input)
            if count < 2:
                print("\nThere should be at least two stations")
                continue
            
            stations = []
            for i in range(count):
                s = input(f"station name {i+1}: ")
                if s == "0":
                    print("\nBake to employee menu")
                    return

                #empty checks (Station)
                if not s:
                    print("\nStation name cannot be empty")
                    continue
                
                if s.lower() in [st.lower() for st in stations]:
                    print("\nThis station has already been entered")
                    return
                
                stations.append(s)

            DataStore.lines.append(
                Line(name=name, origin=origin, destination=destination, stations=stations)

            )

            print("\nLine added successfully") 
            return               
                

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
        while True:
            print("\nAdd train")
            print("Enter 0 to Exit")
            
            train_id = input("Train ID: ")

            if train_id == "0":
                print("\nBake to employee menu")
                return
            
            if not train_id:
                print("\nTrain name cannot be empty")
                continue
            
            if self.train_exists(train_id):
                print("\nThis train already exists")
                continue
            
            line_name = input("Line name: ")

            if line_name == "0":
                print("\nBake to employee menu")
                return
            
            if not line_name:
                print("\nLine name cannot be empty")
                continue
            
            if not self.line_exists(line_name):
                print("\nThis line does not exist")
                continue
            
            average_speed = input("Average speed (km/h): ")

            if average_speed == "0":
                print("\nBake to employee menu")
                return

            if not average_speed:
                print("\nAverage speed cannot be empty")
                continue
            
            if not average_speed.isdigit():
                print("\nPlease enter a valid number for the Average speed")
                continue
            
            average_speed_input = int(average_speed)
            if not 40 <= average_speed_input <= 300:
                print("\nThe average speed should be between 40 to 300 km/h")
                continue
            
            stoppage = input("Stop time: ")

            if stoppage == "0":
                print("\nBake to employee menu")
                return
            
            if not stoppage:
                print("\nStop time cannot be empty")
                continue
            
            if not stoppage.isdigit():
                print("\nPlease enter a valid number for the stoptime")
                continue
            
            quality_level = input("Train level: ")

            if quality_level == "0":
                print("\nBake to employee menu")
                return
            
            if not quality_level:
                print("\nTrain level cannot be empty")
                continue
            
            if not quality_level.isdigit():
                print("\nPlease enter a valid number for the train level")
                continue
            
            quality_level_input = int(quality_level)
            if not 1 <= quality_level_input <= 5:
                print("\nThe quality level should be rated on a scale of 1 to 5")
                continue
            
            price = input("Price: ")

            if price == "0":
                print("\nBake to employee menu")
                return
            
            if not price:
                print("\nPrice cannot be empty")
                continue
            
            if not price.isdigit():
                print("\nPlease enter a valid number for the price")
                continue
            
            price_input = int(price)
            if price_input < 2000:
                print("\nThe price should at least be 2000 Toman")
                continue
            
            capacity = input("Capacity: ")

            if capacity == "0":
                print("\nBake to employee menu")
                return
            
            if not capacity:
                print("\nCapacity cannot be empty")
                continue
            
            if not capacity.isdigit():
                print("\nPlease enter a valid number for the capacity")
                continue
            
            capacity_input = int(capacity)
            if capacity_input < 10:
                print("\nThe capacity should at least be 10")
                continue
            
            DataStore.trains.append(
                Train(
                    train_id=train_id,
                    line_name=line_name,
                    average_speed=average_speed,
                    stoppage=stoppage,
                    quality_level=quality_level,
                    price=price,
                    capacity=capacity
                )
            )
            print("\nTrain added successfully")
            return
    
    def update_train(self):
        while True:
            print("\nUpdate train")
            print("Enter 0 to Exit")

            train_id = input("Train ID: ")

            if train_id == "0":
                print("\nBake to employee menu")
                return
            
            if not train_id:
                print("\nTrain ID cannot be empty")
                continue

            train = self.get_train(train_id)
            if not train:
                print("\nNo train with this ID was found")
                continue

            while True:
                print("\nSelected train information: ")
                print(train)

                print("\nWhich feature do you want to update?")
                print("1. Train ID")
                print("2. Route (Line name)")
                print("3. Average speed")
                print("4. Stoppage (Stop time)")
                print("5. Quality level (Train level)")
                print("6. Price")
                print("7. Capacity")
                print("8. Exit")

                vizhegi = input("choice: ")

                if vizhegi == "1":
                    print("Enter 0 to Exit")

                    new_train_id = input("Enter the new Train ID: ")

                    if new_train_id == "0":
                        continue

                    if not new_train_id or (new_train_id != train.train_id and self.train_exists(new_train_id)):
                        print("\nThe new Train ID is invalid or already exists")
                        continue
                    
                    train.train_id = new_train_id
                    print("\nTrain ID is updated successfully")

                elif vizhegi == "2":
                    print("Enter 0 to Exit")
                    
                    new_line_name = input("Enter the new route (Line name): ")

                    if new_line_name == "0":
                        continue

                    if not new_line_name:
                        print("\nRoute cannot be empty")
                        continue
                    
                    train.line_name = new_line_name
                    print("\nRoute is updated successfully")

                elif vizhegi == "3":
                    print("Enter 0 to Exit")

                    new_average_speed = input("Enter the new average speed: ")

                    if new_average_speed == "0":
                        continue

                    if not new_average_speed:
                        print("\nAverage speed cannot be empty")
                        continue

                    if not new_average_speed.isdigit():
                        print("\nPlease enter a valid number for the Average speed")
                        continue

                    average_speed_input = int(new_average_speed)
                    if not 40 <= average_speed_input <= 300:
                        print("\nThe average speed should be between 40 to 300 km/h")
                        continue

                    train.average_speed = new_average_speed
                    print("\nAverage speed is updated successfully")

                elif vizhegi == "4":
                    print("Enter 0 to Exit")

                    new_stoppage = input("Enter the new stoppage (stop time): ")

                    if new_stoppage == "0":
                        continue

                    if not new_stoppage:
                        print("\nStoppage cannot be empty")
                        continue

                    train.stoppage = new_stoppage
                    print("\nStoppage is updated successfully")

                elif vizhegi == "5":
                    print("Enter 0 to Exit")

                    new_quality_level = input("Enter the new quality level (train level): ")

                    if new_quality_level == "0":
                        continue

                    if not new_quality_level.isdigit():
                        print("\nPlease enter a valid number for the quality_level")
                        continue

                    quality_level_input = int(new_quality_level)
                    if not 1 <= quality_level_input <= 5:
                        print("\nThe quality level should be rated on a scale of 1 to 5")
                        continue

                    if not new_quality_level:
                        print("\nQuality level cannot be empty")
                        continue

                    train.quality_level = new_quality_level
                    print("\nQuality level is updated successfully")

                elif vizhegi == "6":
                    print("Enter 0 to Exit")

                    new_price = input("Enter the new price: ")

                    if new_price == "0":
                        continue

                    if not new_price.isdigit():
                        print("\nPlease enter a valid number for the price")
                        continue

                    price_input = int(new_price)
                    if price_input < 2000:
                        print("\nThe price should at least be 2000 Toman")
                        continue

                    if not new_price:
                        print("\nPrice cannot be empty")
                        continue

                    train.price = new_price
                    print("\nPrice is updated successfully")

                elif vizhegi == "7":
                    print("Enter 0 to Exit")
                    new_capacity = input("Enter the new capacity: ")

                    if new_capacity == "0":
                        continue

                    if not new_capacity.isdigit():
                        print("\nPlease enter a valid number for the capacity")
                        continue

                    capacity_input = int(new_capacity)
                    if capacity_input < 10:
                        print("\nThe capacity should at least be 10")
                        continue

                    if not new_capacity:
                        print("\nCapacity cannot be empty")
                        continue

                    train.capacity = new_capacity
                    print("\nCapacity is updated successfully")
                    
                elif vizhegi == "8":
                    print("\nBake to employee menu")
                    return
                
                else:
                    print("\nInvalid option!")
                    
        
    def delete_train(self):
        while True:
            print("\nDelete train")
            print("Enter 0 to Exit")
            name = input("Enter the name of the train to delete: ")

            if name == "0":
                print("\nBake to employee menu")
                return
            
            if not name:
                print("\nTrain name cannot be empty")
                continue
            
            Tr = self.get_train(name)
            if not Tr:
                print("\nNo train with this name was found")
                continue

            DataStore.trains.remove(Tr)

            print("\nthe train was successfully deleted")
            

    def list_trains(self):
        print("\nList of trains")
        if not DataStore.trains:
            print("\nNo trains have been recorded")
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
    
    def train_exists(self, train_id):
        train_id = train_id.strip().lower()
        return any(t.train_id.strip().lower() == train_id for t in DataStore.trains)

    def get_train(self, train_id):
        train_id = train_id.strip().lower()

        for train in DataStore.trains:
            if train.train_id.strip().lower() == train_id:
                return train
            
        return None                    
