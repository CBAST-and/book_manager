from flask import Flask
from books.books_controller import books_bp

app = Flask(__name__)
app.register_blueprint(books_bp)

@app.route("/")
def home():
    return "Book Manager - CRUD en Flask"

if __name__ == "__main__":
    app.run(debug=True)