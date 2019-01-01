from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
