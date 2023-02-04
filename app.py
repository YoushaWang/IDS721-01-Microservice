from flask import Flask, request
from flask import render_template

app = Flask(__name__)
auths=[]
books=[]

@app.route('/')
def hello():
    print("I am an library search helper")
    return "I am an library search helper:)"

@app.route('/add')
def index():
    return render_template("add.html")

@app.route('/add', methods=['POST'])
def add():
    # global books, auths
    if request.method=='POST':
        auth = request.form['auth']
        book = request.form['book']
        auths.append(auth)
        books.append(book)
        # return f'{i}'
        # redirect('show')
        return render_template("add.html",auths=auths,books=books)

@app.route('/show')
def show():
    # global books, auths
    return render_template("detail.html",auths=auths,books=books)

@app.route('/search')
def searchindex():
    return render_template("search.html")

@app.route('/search', methods=['POST'])
def search():
    # global books, auths
    if request.method=='POST':
        num = request.form['num']
        auth=auths[int(num)]
        book=books[int(num)]
        return render_template("detail_spe.html",auths=auth,books=book)

@app.route('/clear', methods=['GET'])
def clear():
    # global books, auths
    books=[]
    auths=[]
    return render_template("detail.html",auths=[],books=[])

# books = [
#     {
#         "id": 1,
#         "title": "The Great Gatsby",
#         "author": "F. Scott Fitzgerald"
#     },
#     {
#         "id": 2,
#         "title": "To Kill a Mockingbird",
#         "author": "Harper Lee"
#     },
#     {
#         "id": 3,
#         "title": "1984",
#         "author": "George Orwell"
#     }
# ]

# @app.route("/")
# def hello():
#     return "Welcome to the Book Management Microservice"

# @app.route("/books", methods=["GET"])
# def get_books():
#     return jsonify(books)

# @app.route("/books", methods=["POST"])
# def add_book():
#     book = request.get_json()
#     book_id = len(books) + 1
#     book["id"] = book_id
#     books[book_id] = book
#     return "Book added", 201

# @app.route("/books/<int:book_id>", methods=["GET"])
# def get_book(book_id):
#     if book_id in books:
#         return jsonify(books[book_id])
#     else:
#         return "Book not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

# # pip install -r requirements.txt
