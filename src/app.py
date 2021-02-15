from flask import request, Flask, Response, jsonify
from services.generic_proxy.api.generic_service import GenericService
from services.users.api.users_services import UsersService

from services.users.bl.users_manager import UsersManager

app = Flask(__name__)


# region Users Service
@app.route("/create_user", methods=['POST'])
def create_user():
    user = request.get_json()
    users_service = UsersService()

    return users_service.create_user(user)


@app.route("/replace_users_data", methods=['POST'])
def replace_users_data():
    user = request.get_json()
    users_service = UsersService()
    users_service.update_user(user)
    return Response(status=200)


@app.route("/get_user_by_id/<id>", methods=['GET'])
def get_user_by_id(id: int):
    users_service = UsersService()
    return jsonify(users_service.get_user_by_id(id))


@app.route("/get_all_users")
def get_all_users():
    users_service = UsersService()
    return jsonify(users_service.get_all_users())


# endregion Users service


# region Generic Service

@app.route("/create", methods=['POST'])
def create():
    request_obj = request.get_json()
    return GenericService(request_obj['collection_name']).create(request_obj['data'])


@app.route("/replace", methods=['POST'])
def replace():
    request_obj = request.get_json()
    GenericService(request_obj['collection_name']).replace(request_obj['data'])
    return Response(status=200)


@app.route("/get_by_id/<id>", methods=['GET'])
def get_by_id(id: int):
    request_obj = request.get_json()
    return jsonify(GenericService(request_obj['collection_name']).get_by_id(id))


@app.route("/get_all")
def get_all():
    request_obj = request.get_json()
    return jsonify(GenericService(request_obj['collection_name']).get_all())

# endregion Generic Service


@app.route("/", methods=['GET'])
def hello_world():
    return 'hello world'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
