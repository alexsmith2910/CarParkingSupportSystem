from pymongo import MongoClient

from src.config.get_json_data import get_data as CONFIG


class DatabaseClient:
    _loaded = {}
    database = None

    def __new__(cls, mongo_client):
        if (client := cls._loaded.get(mongo_client)) is not None:
            print(f"Returning existing client from cache ({mongo_client})")
            return client

        client = super().__new__(cls)
        client_init = client._init_from_client(mongo_client)

        if client_init is None:
            return None
        else:
            cls._loaded[mongo_client] = client._init_from_client(mongo_client)
            return client

    def __init__(self, mongo_client):
        self.database = self._loaded[mongo_client]

    def insert_one(self, data):
        """
        DatabaseClient.insert_one(data) uses MongoClient to insert a singular dictionary.\n
        :param data: dict() || {...}
        """
        self.database.insert_one(data)

    def insert_many(self, data):
        """
        DatabaseClient.insert_many(data) uses MongoClient to insert multiple dictionaries in a list.\n
        :param data: list() || [{...}, ...]
        """
        self.database.insert_many(data)

    def find_one(self, data):
        """
        DatabaseClient.find_one(data) uses MongoClient to find a singular item in the database.\n
        :param data: dict() || {...}
        """
        return self.database.find_one(data)

    def find(self, data):
        """
        DatabaseClient.find(data) uses MongoClient to find all items in the database that match.\n
        :param data: dict() || {...}
        """
        return self.database.find(data)

    def delete_one(self, data):
        """
        DatabaseClient.delete_one(data) uses MongoClient to delete the item that matches.\n
        :param data: dict() || {...}
        """
        return self.database.delete_one(data)

    def delete_many(self, data):
        """
        DatabaseClient.delete_many(data) uses MongoClient to delete all items that match.\n
        :param data: dict() || {...}
        """
        return self.database.delete_many(data)

    def update_one(self, data, new_data):
        """
        DatabaseClient.update_one(data) uses MongoClient to update the item that matches with new data.\n
        :param data: dict() || {...}
        :param new_data: dict() || {...}
        """
        return self.database.delete_one({data, new_data})

    @staticmethod
    def _init_from_client(db_name):
        try:
            client = MongoClient()[CONFIG("db_config")["client"]][db_name]
            return client
        except Exception as e:
            return None
