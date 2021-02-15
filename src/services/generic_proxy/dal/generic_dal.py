
from typing import Dict

from bson.objectid import ObjectId

from common.db.db_connection_manager import MongoConnectionClient
import json
from bson import ObjectId

from common.helpers.json_encoder import JSONEncoder


class GenericDAL:
    def __init__(self, collection_name: str):
        client = MongoConnectionClient().client
        db = client['salon_app']
        self._collection = db[collection_name]

    def create(self, model: Dict):
        model_id = self._collection.insert_one(model).inserted_id
        return str(model_id)

    def get_by_id(self, model_id: str):
        object_id = ObjectId(model_id)
        model = self._collection.find_one({"_id": object_id})
        model_json = JSONEncoder().encode(model)
        return json.loads(model_json)

    def get_all(self):
        models = self._collection.find({})
        result = [json.loads(JSONEncoder().encode(model)) for model in models]
        return result

    def replace(self, model: Dict):
        id = ObjectId(model['_id'])
        del(model['_id'])
        replace_one_result = self._collection.replace_one({"_id": id}, model)
        return replace_one_result

    def delete(self, model_id: str):
        object_id = ObjectId(model_id)
        self._collection.delete_one({"_id": object_id})
