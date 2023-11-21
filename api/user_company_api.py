
from models.user import User
from models.company import Company

class UserCompanyAPI:
    def create_user(self, name, role):
        new_user = User(name, role)
        return new_user

    def create_company(self, name):
        new_company = Company(name)
        return new_company

