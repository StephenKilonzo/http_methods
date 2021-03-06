from flask import *

app = Flask(__name__)


@app.route('/table/<int:num>')
def table(num):
    return render_template('delimiter.html', n=num)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
