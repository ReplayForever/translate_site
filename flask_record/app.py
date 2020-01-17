from flask import Flask, render_template
from flask import Response
from os import path


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')


@app.route('/dist/<file>')
def get_file(file):
    with open(path.join('dist', file), 'rb') as f:
        return Response(f.read())
