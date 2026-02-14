
import re
from datetime import datetime
from BANK import API

bank_api = API()


# ------------------ validators ------------------
def validate_email(email: str) -> bool:
    email = email.strip()
    if "@" not in email:
        return False
    # divides the string into three parts
    local, _, domain = email.partition("@")
    if not local or not domain:
        return False
    # must have a dot in domain and non-empty parts
    if "." not in domain:
        return False
    d1, _, d2 = domain.rpartition(".")
    return bool(d1) and bool(d2)


def validate_password(pw: str) -> bool:
    # must contain: English letters, digits, and @ or &
    has_letter = re.search(r"[A-Za-z]", pw) is not None
    has_digit = re.search(r"\d", pw) is not None
    has_special = re.search(r"[@&]", pw) is not None
    return has_letter and has_digit and has_special


# ------------------ helpers ------------------
# do not empty input
def input_non_empty(msg: str) -> str:
    while True:
        val = input(msg).strip()
        if val:
            return val
        print("Input cannot be empty.")

#convert date system to string and used the file name
#because file name is uniqe
def now_str() -> str:
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#append a text in a filename
def save_text_append(filename: str, text: str):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text + "\n")

#list of trains as file text (save)
def export_available_trains(trains: dict, filename: str = "available_trains.txt"):
    lines = []
    lines.append("AVAILABLE TRAINS")
    lines.append(f"Generated at: {datetime.now()}")
    lines.append("-" * 60)
    for tid, t in trains.items():
        status = "FULL" if t["capacity"] <= 0 else "OK"
        lines.append(
            f"ID:{tid} | Train:{t['name']} | Dest:{t['dest']} | "
            f"Cap:{t['capacity']} | Price:{t['price']} | {status}"
        )
    lines.append("-" * 60)
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


# ------------------ BANK integration ------------------
def bank_pay_and_get_payment_id(card_info: dict, amount: int) -> str | None:
    """
    Returns payment_id if valid, otherwise None.
    BANK.py:
      pay(card, exp_month, exp_year, password, cvv2, amount)
    """
    try:
        payment_id = bank_api.pay(
            card=card_info["card"],
            exp_month=card_info["exp_month"],
            exp_year=card_info["exp_year"],
            password=card_info["password"],
            cvv2=card_info["cvv2"],
            amount=amount
        )
        return payment_id
    except ValueError:
        return None


def input_card_info() -> dict | None:
    """
    Reads card fields required by BANK.py and returns a dict, or None if invalid format.
    """
    print("\n--- Add New Card (BANK) ---")
    card = input_non_empty("Card (16 digits): ")
    exp_month = input_non_empty("Exp Month (1-12): ")
    exp_year = input_non_empty("Exp Year (1403-1408): ")
    password = input_non_empty("Card Password (6 digits): ")
    cvv2 = input_non_empty("CVV2 (3 digits): ")

    # basic numeric validation to avoid crashes
    if not (card.isdigit() and exp_month.isdigit() and exp_year.isdigit() and password.isdigit() and cvv2.isdigit()):
        print("All fields must be numeric.")
        return None

    info = {
        "card": int(card),
        "exp_month": int(exp_month),
        "exp_year": int(exp_year),
        "password": int(password),
        "cvv2": int(cvv2),
    }

    # BANK validate rules
    if not bank_api.validate(**info):
        print("Invalid card details based on BANK rules.")
        return None

    return info


def add_new_card_to_user(user: dict) -> bool:
    info = input_card_info()
    if info is None:
        return False

    # prevent duplicate same card (optional but nice)
    for c in user["cards"]:
        if c["card"] == info["card"] and c["exp_month"] == info["exp_month"] and c["exp_year"] == info["exp_year"]:
            print("This card is already saved.")
            return True

    user["cards"].append(info)
    print("Card saved successfully.")
    return True



