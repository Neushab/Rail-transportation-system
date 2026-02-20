class User:
    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password

    def __str__(self):
        return f"{self.first_name} {self.last_name} | Username: {self.username} | Password: {self.password} | Email: {self.email}"
    
        
class Employee(User):
    pass
