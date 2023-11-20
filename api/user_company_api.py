
from models.user import User
from models.company import Company

class UserCompanyAPI:
    def create_user(self, name, role):
        new_user = User(name, role)
        # Logic to store the new user in a database or data structure
        return new_user

    def create_company(self, name):
        new_company = Company(name)
        # Logic to store the new company in a database or data structure
        return new_company

