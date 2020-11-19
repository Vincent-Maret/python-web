from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)


def loadJson(path):
    f = open(path)
    loadedJson = json.load(f)
    f.close()
    return loadedJson


booksList = loadJson('data/books.json')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/books")
def books():
    return jsonify(booksList)


@app.route('/books/<id>')
def getBook(id):
    searchedBook = next(
        (book for book in booksList if book["isbn"] == id), False)
    if searchedBook:
        return render_template('book.html', book=searchedBook)
    else:
        return 'Book not found', 404


@app.route('/books/title/<title>')
def getBookByTitle(title):
    searchedBook = next(
        (book for book in booksList if book["title"] == title), False)
    if searchedBook:
        return render_template('book.html', book=searchedBook)
    else:
        return 'Book not found', 404


if __name__ == '__main__':
    app.run(debug=True)
