from panels.admin_panel import AdminPanel
from panels.employee_panel import EmployeePanel
from panels.user_panel import NormalUserPanel
def main():
    while True:
        print("\nRailway Transportation System")
        print("1. Admin")
        print("2. Train Employee")
        print("3. User")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            AdminPanel().run()
        elif choice == "2":
            EmployeePanel().run()
        elif choice == "3":
            NormalUserPanel().run()
        elif choice == "4":
            print("Goodbye :)")
            break
        else:
            print("\nInvalid option!")
            

if __name__ == "__main__":
    main()