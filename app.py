from flask import Flask, render_template
from books.books_controller import books_bp

app = Flask(__name__)
app.register_blueprint(books_bp)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)