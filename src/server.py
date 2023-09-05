from uuid import uuid4

from flask import Flask
from flask import request
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app,
    x_for=1,
    x_proto=1,
    x_host=1,
    x_prefix=1,
)


@app.get("/")
def index():
    return b"""<!DOCTYPE html>
<html>
    <body>
        Hello, World!
    </body>
</html>
"""


books = {}


@app.post("/books")
def create_book():
    book = request.json
    book_id = str(uuid4())
    books[book_id] = book
    return ("", 201, {"Location": f"/books/{book_id}"})


@app.get("/books/<string:book_id>")
def get_book(book_id):
    if book_id in books:
        return books[book_id]
    return "", 404


@app.delete("/books/<string:book_id>")
def delete_book(book_id):
    del books[book_id]
    return "", 204
