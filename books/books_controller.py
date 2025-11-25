from flask import Blueprint, request, render_template, redirect

books_bp = Blueprint("books", __name__)

books = []  # Base de datos temporal

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


@books_bp.route("/books", methods=["GET"])
def list_books():
    return render_template("list_books.html", books=books)

@books_bp.route("/books/edit/<int:book_id>", methods=["GET"])
def edit_book_form(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return "Libro no encontrado", 404

    return render_template("edit_book.html", book=book)


@books_bp.route("/books/edit/<int:book_id>", methods=["POST"])
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return "Libro no encontrado", 404

    book["title"] = request.form.get("title")
    book["author"] = request.form.get("author")
    book["pdf_url"] = request.form.get("pdf_url")

    return redirect("/books")

@books_bp.route("/books/delete/<int:book_id>", methods=["POST"])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return redirect("/books")

