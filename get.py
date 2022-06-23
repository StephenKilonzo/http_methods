from flask import *

app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    user_name = request.args.get('user_name')
    password = request.args.get('pass')
    if user_name == "steve" and password == "1234":
        return f'Welcome {user_name}'


if __name__ == '__main__':
    app.run(debug=True)
