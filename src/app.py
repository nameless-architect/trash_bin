from flask import request, Flask, Response, jsonify

from services.users.bl.users_manager import UsersManager

app = Flask(__name__)


@app.route("/create_user", methods=['POST'])
def create_user():
    manager = UsersManager.construct()
    user = request.get_json()

    return manager.create_user(user)


@app.route("/replace_users_data", methods=['POST'])
def replace_users_data():
    manager = UsersManager.construct()
    user = request.get_json()

    manager.upadate_user(user)
    return Response(status=200)


@app.route("/get_user_by_id/<id>", methods=['GET'])
def get_user_by_id(id: int):
    manager = UsersManager.construct()
    return manager.get_user_by_id(id)


@app.route("/get_all_users")
def get_all_users():
    manager = UsersManager.construct()
    return jsonify(manager.get_all_users())

@app.route("/", methods=['GET'])
def hello_world():
    return 'hello world'


if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 80, debug = True) 