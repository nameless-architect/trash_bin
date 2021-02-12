from abc import ABC, abstractmethod


class UsersServiceContract(ABC):

    @abstractmethod
    def create_user(self, user: dict):
        pass

    @abstractmethod
    def update_user(self, user_data):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id):
        pass

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def delete_user(self, user_id):
        pass

    @abstractmethod
    def filter_users(self, filter_expresion: str):
        pass
