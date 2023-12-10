from pymongo import MongoClient
from models.user import User

class UserRepository:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['your_database_name']
        self.users_collection = self.db['users']

    def create_user(self, user):
        user_data = {
            'username': user.username,
            'email': user.email
        }
        result = self.users_collection.insert_one(user_data)
        return str(result.inserted_id)

    def get_all_users(self):
        users = self.users_collection.find()
        return [User(user['username'], user['email']) for user in users]

    def get_user_by_id(self, user_id):
        user_data = self.users_collection.find_one({'_id': user_id})
        return User(user_data['username'], user_data['email']) if user_data else None

    def update_user(self, user_id, updated_user):
        update_data = {
            'username': updated_user.username,
            'email': updated_user.email
        }
        result = self.users_collection.update_one({'_id': user_id}, {'$set': update_data})
        return result.modified_count > 0

    def delete_user(self, user_id):
        result = self.users_collection.delete_one({'_id': user_id})
        return result.deleted_count > 0
