

from common.communication.users_service_contract import UsersServiceContract
from services.users.bl.users_manager import UsersManager


class UsersService(UsersServiceContract):

    def create_user(self, user: dict):
        users_manger = UsersManager.construct()
        return users_manger.create_user(user)

    def update_user(self, user_data):
        users_manger = UsersManager.construct()
        return users_manger.upadate_user(user_data)

    def get_user_by_id(self, user_id: str):
        users_manger = UsersManager.construct()
        return users_manger.get_user_by_id(user_id)

    def get_all_users(self):
        users_manger = UsersManager.construct()
        return users_manger.get_all_users()

    def delete_user(self, user_id: str):
        users_manger = UsersManager.construct()
        return users_manger.delete_user(user_id)

    def filter_users(self, filter_expresion: str):
        users_manger = UsersManager.construct()
        return users_manger.filter_users(filter_expresion)
