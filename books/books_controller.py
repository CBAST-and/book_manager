from flask import Blueprint, request, render_template, redirect

books_bp = Blueprint("books", __name__)

books = []

@books_bp.route("/books/add", methods=["GET"])
def add_book_form():
    return render_template("add_book.html")

@books_bp.route("/books/add", methods=["POST"])
def add_book():
    title = request.form.get("title")
    author = request.form.get("author")
    pdf_url = request.form.get("pdf_url")

    new_book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "pdf_url": pdf_url
    }

    books.append(new_book)

    return redirect("/books/add")