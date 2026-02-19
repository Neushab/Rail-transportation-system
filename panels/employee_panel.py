from core.data_store import DataStore
from core.railway import Line, Train


class EmployeePanel:

    # ================= RUN =================
    def run(self):
        print("\nEmployee Panel")

        if not self.employee_login():
            return

        while True:
            self.employee_menu()
            choice = input("Choose an option: ").strip()

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
                return
            else:
                print("Invalid option!")

    # ================= LOGIN =================
    def employee_login(self):
        if not DataStore.employees:
            print("No employees registered yet.")
            return False

        username = input("Employee username: ").strip()
        password = input("Employee password: ").strip()

        for emp in DataStore.employees:
            if emp.username == username and emp.password == password:
                print("Employee logged in successfully!")
                return True

        print("Invalid username or password.")
        return False

    # ================= MENU =================
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

    # ================= LINE METHODS =================
    def add_line(self):
        print("\nAdd Line")

        name = input("Line name: ").strip()
        if not name:
            print("Line name required.")
            return

        if self.get_line(name):
            print("Line already exists.")
            return

        origin = input("Origin: ").strip()
        destination = input("Destination: ").strip()

        count = input("Number of stations: ").strip()
        if not count.isdigit() or int(count) <= 0:
            print("Invalid station count.")
            return

        stations = []
        for i in range(int(count)):
            s = input(f"Station {i+1}: ").strip()
            stations.append(s)

        DataStore.lines.append(Line(name, origin, destination, stations))
        print("Line added successfully!")

    def list_lines(self):
        print("\nLines:")
        if not DataStore.lines:
            print("No lines recorded.")
            return

        for line in DataStore.lines:
            print(line)

    def get_line(self, name):
        for line in DataStore.lines:
            if line.name.lower() == name.lower():
                return line
        return None

    def update_line(self):
        print("\nUpdate Line")

        name = input("Line name: ").strip()
        line = self.get_line(name)

        if not line:
            print("Line not found.")
            return

        line.origin = input("New origin: ").strip()
        line.destination = input("New destination: ").strip()

        print("Line updated successfully!")

    def delete_line(self):
        print("\nDelete Line")

        name = input("Line name: ").strip()
        line = self.get_line(name)

        if not line:
            print("Line not found.")
            return

        DataStore.lines.remove(line)

        # ✅ حذف قطارهای مربوط به این خط
        DataStore.trains = [
            t for t in DataStore.trains
            if t.line_name.lower() != name.lower()
        ]

        print("Line and related trains deleted successfully!")

    # ================= TRAIN METHODS =================
    def add_train(self):
        print("\nAdd Train")

        train_id = input("Train ID: ").strip()
        if not train_id:
            print("Train ID required.")
            return

        # ✅ چون trains لیست است
        if any(t.train_id == train_id for t in DataStore.trains):
            print("Train ID already exists!")
            return

        train_name = input("Train name: ").strip()

        line_name = input("Line name: ").strip()
        if not self.get_line(line_name):
            print("Line does not exist. Add line first.")
            return

        speed = input("Speed: ").strip()
        stoptime = input("Stop time (minutes): ").strip()
        level = input("Train level: ").strip()
        price = input("Price: ").strip()
        capacity = input("Capacity: ").strip()

        if not (speed.isdigit() and stoptime.isdigit()
                and price.isdigit() and capacity.isdigit()):
            print("Speed, StopTime, Price, Capacity must be numeric.")
            return

        new_train = Train(
            train_id,
            train_name,
            line_name,
            int(speed),
            int(stoptime),
            level,
            int(price),
            int(capacity)
        )

        DataStore.trains.append(new_train)

        print("Train added successfully!")

    def list_trains(self):
        print("\nTrains:")
        if not DataStore.trains:
            print("No trains recorded.")
            return

        for train in DataStore.trains:
            print(train)

    def update_train(self):
        print("\nUpdate Train")

        train_id = input("Train ID: ").strip()

        train = next((t for t in DataStore.trains if t.train_id == train_id), None)

        if not train:
            print("Train not found.")
            return

        new_price = input("New price: ").strip()
        if not new_price.isdigit():
            print("Price must be numeric.")
            return

        train.price = int(new_price)
        print("Train updated successfully!")

    def delete_train(self):
        print("\nDelete Train")

        train_id = input("Train ID: ").strip()

        train = next((t for t in DataStore.trains if t.train_id == train_id), None)

        if not train:
            print("Train not found.")
            return

        DataStore.trains.remove(train)
        print("Train deleted successfully!")