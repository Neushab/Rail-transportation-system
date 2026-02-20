from core.data_store import DataStore
from core.validators import validate_email, validate_password
from datetime import datetime
from panels.BANK import API

bank_api = API()


class NormalUserPanel:

    # ================= MAIN PANEL =================
    def run(self):
        while True:
            print("\n=== Normal User Panel ===")
            print("1. Register")
            print("2. Login")
            print("3. Back")

            choice = input("Choice: ").strip()

            if choice == "1":
                self.register()
            elif choice == "2":
                user = self.login()
                if user:
                    self.purchase_panel(user)
            elif choice == "3":
                return
            else:
                print("Invalid choice!")

    # ================= REGISTER =================
    def register(self):
        print("\n--- Register ---")

        name = input("Name: ").strip()
        email = input("Email: ").strip()
        username = input("Username: ").strip()
        password = input("Password (letters + digits + @ or &): ").strip()

        if not all([name, email, username, password]):
            print("All fields are required.")
            return

        if not validate_email(email):
            print("Invalid email format!")
            return

        if not validate_password(password):
            print("Password must contain letters + digits + @ or &")
            return

        if any(u["username"].lower() == username.lower() for u in DataStore.users):
            print("Username already exists!")
            return

        if any(u["email"].lower() == email.lower() for u in DataStore.users):
            print("Email already exists!")
            return

        new_user = {
            "name": name,
            "email": email,
            "username": username,
            "password": password,
            "wallet": 0,
            "cards": []
        }

        DataStore.users.append(new_user)
        print("Registration successful!")

    # ================= LOGIN =================
    def login(self):
        print("\n--- Login ---")

        username = input("Username (or 'back'): ").strip()
        if username.lower() == "back":
            return None

        password = input("Password: ").strip()

        for u in DataStore.users:
            if u["username"] == username and u["password"] == password:
                print("Login successful!")
                return u

        print("Invalid username or password!")
        return None

    # ================= PURCHASE PANEL =================
    def purchase_panel(self, user):
        while True:
            print("\n=== Purchase Panel ===")
            print(f"User: {user['name']} | Wallet: {user['wallet']}")
            print("1. Buy Ticket")
            print("2. Edit Profile")
            print("3. Wallet")
            print("4. Logout")

            choice = input("Choice: ").strip()

            if choice == "1":
                self.buy_ticket(user)
            elif choice == "2":
                self.edit_profile(user)
            elif choice == "3":
                self.wallet_panel(user)
            elif choice == "4":
                print("Logged out.")
                return
            else:
                print("Invalid choice!")

    # ================= WALLET PANEL =================
    def wallet_panel(self, user):
        while True:
            print("\n=== Wallet Panel ===")
            print(f"Balance: {user['wallet']}")
            print("1. Charge with saved card")
            print("2. Add new card")
            print("3. Back")

            choice = input("Choice: ").strip()

            if choice == "3":
                return

            if choice == "2":
                self.add_new_card(user)
                continue

            if choice != "1":
                print("Invalid choice.")
                continue

            if not user["cards"]:
                print("No saved cards. Please add a card first.")
                continue

            print("\n--- My Cards ---")
            for i, c in enumerate(user["cards"], start=1):
                masked = "****" * 3 + str(c["card"])[-4:]
                print(f"{i}. {masked} | exp:{c['exp_month']}/{c['exp_year']}")

            idx = input("Select card number: ").strip()
            if not idx.isdigit() or not (1 <= int(idx) <= len(user["cards"])):
                print("Invalid selection.")
                continue

            amount_str = input("Amount to charge: ").strip()
            if not amount_str.isdigit() or int(amount_str) <= 0:
                print("Invalid amount.")
                continue

            amount = int(amount_str)
            selected_card = user["cards"][int(idx) - 1]

            try:
                payment_id = bank_api.pay(amount=amount, **selected_card)
            except ValueError:
                print("Payment failed.")
                continue

            user["wallet"] += amount

            log_text = (
                f"{datetime.now()} | CHARGE | +{amount} | "
                f"Balance={user['wallet']} | payment_id={payment_id}\n"
            )

            with open(f"transactions_{user['username']}.txt", "a", encoding="utf-8") as f:
                f.write(log_text)

            print("Wallet charged successfully.")
            print(f"Payment ID: {payment_id}")

    # ================= ADD NEW CARD =================
    def add_new_card(self, user):
        print("\n--- Add New Card ---")

        card = input("Card (16 digits): ").strip()
        exp_month = input("Exp Month (1-12): ").strip()
        exp_year = input("Exp Year (1403-1408): ").strip()
        password = input("Card Password (6 digits): ").strip()
        cvv2 = input("CVV2 (3 digits): ").strip()

        if not (card.isdigit() and exp_month.isdigit() and exp_year.isdigit()
                and password.isdigit() and cvv2.isdigit()):
            print("All fields must be numeric.")
            return

        card_info = {
            "card": int(card),
            "exp_month": int(exp_month),
            "exp_year": int(exp_year),
            "password": int(password),
            "cvv2": int(cvv2)
        }

        if not bank_api.validate(**card_info):
            print("Invalid card details!")
            return

        if any(c["card"] == card_info["card"] for c in user["cards"]):
            print("This card is already saved.")
            return

        user["cards"].append(card_info)
        print("Card saved successfully.")

    # ================= BUY TICKET =================
    def buy_ticket(self, user):

        if not DataStore.trains:
            print("No trains available!")
            return

        print("\n--- Available Trains ---")
        for i, t in enumerate(DataStore.trains, start=1):
            print(f"{i}. {t}")

        train_id = input("Enter Train ID (or 'back'): ").strip()
        if train_id.lower() == "back":
            return

        train = next((x for x in DataStore.trains if str(x.train_id) == train_id), None)

        if not train:
            print("Train not found!")
            return

        if train.remaining_capacity <= 0:
            print("Train is FULL!")
            return

        count_input = input("How many tickets?: ").strip()
        if not count_input.isdigit() or int(count_input) <= 0:
            print("Invalid ticket count.")
            return

        count = int(count_input)

        if count > train.remaining_capacity:
            print("Not enough seats available.")
            return

        total = count * train.price

        if user["wallet"] < total:
            print("Insufficient wallet balance.")
            return

        # Finalize purchase
        user["wallet"] -= total
        train.remaining_capacity -= count

        purchase_time = datetime.now()

        ticket_text = (
            f"Ticket Issue Time: {purchase_time}\n"
            f"Buyer: {user['name']} (username={user['username']})\n"
            f"Train: {train.name} | ID: {train.train_id}\n"
            f"Line: {train.line_name}\n"
            f"Tickets Count: {count}\n"
            f"Price (each): {train.price}\n"
            f"Total Paid: {total}\n"
            f"Remaining Wallet: {user['wallet']}\n"
            f"{'-'*60}\n"
        )

        filename = f"ticket_{user['username']}_{purchase_time.strftime('%Y%m%d_%H%M%S')}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(ticket_text)

        log_text = (
            f"{purchase_time} | BUY | Train={train.train_id} | "
            f"-{total} | Balance={user['wallet']}\n"
        )

        with open(f"transactions_{user['username']}.txt", "a", encoding="utf-8") as f:
            f.write(log_text)

        print("Purchase successful!")
        print(f"Ticket saved to: {filename}")

    # ================= EDIT PROFILE =================
    def edit_profile(self, user):
        while True:
            print("\n=== Edit Profile ===")
            print(f"Username (fixed): {user['username']}")
            print(f"1. Name: {user['name']}")
            print(f"2. Email: {user['email']}")
            print("3. Password")
            print("4. Back")

            choice = input("Choice: ").strip()

            if choice == "1":
                user["name"] = input("New name: ").strip()
                print("Name updated.")

            elif choice == "2":
                new_email = input("New email: ").strip()
                if not validate_email(new_email):
                    print("Invalid email format.")
                elif any(u["email"].lower() == new_email.lower() and u != user for u in DataStore.users):
                    print("Email already in use.")
                else:
                    user["email"] = new_email
                    print("Email updated.")

            elif choice == "3":
                new_password = input("New password: ").strip()
                if not validate_password(new_password):
                    print("Password must contain letters + digits + @ or &")
                else:
                    user["password"] = new_password
                    print("Password updated.")

            elif choice == "4":
                return
            else:
                print("Invalid choice!")