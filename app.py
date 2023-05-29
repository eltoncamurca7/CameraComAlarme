from flask import Flask, Response, request
from test import Segurança


app = Flask(__name__)


@app.route('/alarm', methods=['GET'])
def alarm():
    return Segurança.test()


if __name__ == '__main__':
    app.run(debug=True)