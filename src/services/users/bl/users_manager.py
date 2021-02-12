

from services.users.dal.users_dal import UsersDAL


class UsersManager:

    def __init__(self, users_dal: UsersDAL) -> None:
        self._users_dal = users_dal

    def create_user(self, user: dict):
        return self._users_dal.create_user(user)

    def update_user(self, user_data):
        return self._users_dal.update_user(user_data)

    def get_user_by_id(self, user_id):
        return self._users_dal.get_user(user_id)

    def get_all_users(self):
        return self._users_dal.get_all_users()

    def delete_user(self, user_id):
        pass

    def filter_users(self, filter_expresion: str):
        pass

    @classmethod
    def construct(cls):
        users_dal = UsersDAL()
        return cls(users_dal)
