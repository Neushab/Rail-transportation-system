from core.data_store import DataStore
from panels.admin_panel import AdminPanel
from panels.employee_panel import EmployeePanel

def main():
    store = DataStore()

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
            print("پنل کاربر هنوز پیاده‌سازی نشده.")
        elif choice == "4":
            print("exit")
            break
        else:
            print("گزینه نامعتبر است.")
            

if __name__ == "__main__":
    main()


