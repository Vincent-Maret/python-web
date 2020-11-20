from flask import Flask, render_template, jsonify
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/hello/<name>")
def hello(name):
    return render_template('helloName.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)