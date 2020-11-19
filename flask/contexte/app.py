from flask import Flask, render_template, jsonify
app = Flask(__name__)

booksList = [
    {
        'id': 1,
        'titre': 'un titre',
    },
    {
        'id': 2,
        'titre': 'un autre titre random',
    }
]


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/books")
def books():
    return jsonify(booksList)


@app.route('/books/<id>')
def getBook(id):
    searchedBook = next(
        (book for book in booksList if book["id"] == int(id)), False)
    if searchedBook:
        return jsonify(searchedBook)
    else:
        return 'Book not found', 404


@app.route('/books/name/<name>')
def getBookByName(name):
    searchedBook = next(
        (book for book in booksList if book["titre"] == name), False)
    if searchedBook:
        return jsonify(searchedBook)
    else:
        return 'Book not found', 404


if __name__ == '__main__':
    app.run(debug=True)
