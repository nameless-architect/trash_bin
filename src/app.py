from flask import request, Flask, Response



app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return 'hello worlds'


if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 80, debug = True) 