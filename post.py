from flask import *

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    user_name = request.form['user_name']
    password = request.form['pass']
    if user_name == "steve" and password == "1234":
        return f'Welcome {user_name}'


if __name__ == '__main__':
    app.run(debug=True)
