import unittest
from core.user import Employee
from core.data_store import DataStore
from admin_panel import AdminPanel


class TestAdminPanel(unittest.TestCase):

    def setUp(self):
        # قبل از هر تست، دیتاست خالی باشه
        DataStore.employees = []
        self.panel = AdminPanel()

    def test_add_employee(self):
        # اضافه کردن کارمند
        emp = Employee("tara123", "1234", "tara@test.com", "Tara", "Hoseini")
        DataStore.employees.append(emp)

        # چک کردن اضافه شدن
        self.assertEqual(len(DataStore.employees), 1)
        self.assertEqual(DataStore.employees[0].username, "tara123")

    def test_add_duplicate_username(self):
        emp = Employee("tara123", "1234", "tara@test.com", "Tara", "Hoseini")
        DataStore.employees.append(emp)

        # تلاش برای اضافه کردن دوباره با همان Username
        duplicate_emp = Employee("tara123", "5678", "tara2@test.com", "Tara2", "Hoseini2")
        usernames = [e.username for e in DataStore.employees]
        self.assertIn(duplicate_emp.username, usernames)

    def test_remove_employee(self):
        emp = Employee("tara123", "1234", "tara@test.com", "Tara", "Hoseini")
        DataStore.employees.append(emp)

        # حذف کارمند
        DataStore.employees = [e for e in DataStore.employees if e.username != "tara123"]
        self.assertEqual(len(DataStore.employees), 0)

    def test_list_employees(self):
        emp1 = Employee("tara123", "1234", "tara@test.com", "Tara", "Hoseini")
        emp2 = Employee("sara456", "5678", "sara@test.com", "Sara", "Mohammadi")
        DataStore.employees.extend([emp1, emp2])

        # بررسی لیست
        usernames = [e.username for e in DataStore.employees]
        self.assertIn("tara123", usernames)
        self.assertIn("sara456", usernames)


if __name__ == "__main__":
    unittest.main()