from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Book Manager - CRUD en Flask"

if __name__ == "__main__":
    app.run(debug=True)