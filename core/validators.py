import re

def validate_email(email: str) -> bool:
    # "email" must contain '@' and a domain with '.'
    if not isinstance(email, str):
        return False
    email = email.strip()
    if "@" not in email:
        return False
    local, _, domain = email.partition("@")
    if not local or not domain or "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    return True

def validate_password(password: str) -> bool:
    """
    password rule:
    - includes English letters
    - includes digits
    - includes '@' or '&'
    """
    if not isinstance(password, str):
        return False
    password = password.strip()
    has_letter = re.search(r"[A-Za-z]", password) is not None
    has_digit = re.search(r"\d", password) is not None
    has_symbol = ("@" in password) or ("&" in password)
    return has_letter and has_digit and has_symbol


