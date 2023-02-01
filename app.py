from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee"
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell"
    }
]

@app.route("/")
def hello():
    return "Welcome to the Book Management Microservice"

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

@app.route("/books", methods=["POST"])
def add_book():
    book = request.get_json()
    book_id = len(books) + 1
    book["id"] = book_id
    books[book_id] = book
    return "Book added", 201

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    if book_id in books:
        return jsonify(books[book_id])
    else:
        return "Book not found", 404

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
# from flask import Flask, request

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello, World!"

# @app.route("/reverse", methods=["POST","GET"])
# def reverse():
#     text="Hello, World!"
#     # text = request.get_json()["text"]
#     reversed_text = text[::-1]
#     # return {"reversed_text": reversed_text}
#     return reversed_text
