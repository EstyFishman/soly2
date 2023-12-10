from models.user import User
from repositories.user_repository import UserRepository

class UserController:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, username, email):
        new_user = User(username, email)
        self.user_repository.create_user(new_user)

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def update_user(self, user_id, username, email):
        updated_user = User(username, email)
        self.user_repository.update_user(user_id, updated_user)

    def delete_user(self, user_id):
        self.user_repository.delete_user(user_id)
