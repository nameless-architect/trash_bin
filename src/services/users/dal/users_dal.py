
from typing import Dict

from bson.objectid import ObjectId

from common.db.db_connection_manager import MongoConnectionClient
import json
from bson import ObjectId



class UsersDAL:
    def __init__(self):
        client = MongoConnectionClient().client
        db = client['salon_app']
        self._collection = db['users']

    def create_user(self, user: Dict):
        new_user_id = self._collection.insert_one(user).inserted_id
        return str(new_user_id)

    def get_user(self, user_id: str):
        object_id = ObjectId(user_id)
        user = self._collection.find_one({"_id": object_id})
        user_json = JSONEncoder().encode(user)
        return json.loads(user_json)

    def get_all_users(self):
        users = self._collection.find({})
        result = [json.loads(JSONEncoder().encode(user)) for user in users]
        return result

    def update_user(self, user: Dict):
        id = ObjectId(user['_id'])
        del(user['_id'])
        replace_one_result = self._collection.replace_one({"_id": id}, user)
        return replace_one_result
