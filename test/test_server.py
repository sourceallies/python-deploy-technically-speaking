from uuid import *

import pytest
import requests


def test_simple_index_page(base_server_url: str):
    resp = requests.get(base_server_url + "/")
    
    assert True is resp.ok
    assert resp.headers.get("Content-Type") == "text/html; charset=utf-8"
    assert resp.content == b"""<!DOCTYPE html>
<html>
    <body>
        Hello, World!
    </body>
</html>
"""


def test_create_a_book(base_server_url: str):
    resp = requests.post(base_server_url + "/books", json={
        "title": "Moby Dick",
        "author": "Herman Melville"
    })

    assert resp.status_code == 201
    assert not resp.content


def test_create_and_retrieve_book(base_server_url: str):
    resp = requests.post(base_server_url + "/books", json={
        "title": "Moby Dick",
        "author": "Herman Melville"
    })

    uuid_str = resp.headers.get("Location").split("/books/")[-1]

    try:
        UUID(uuid_str)
    except Exception:
        pytest.fail("UUID malformed")

    retrieve = requests.get(base_server_url + "/books/" + uuid_str)

    assert retrieve.status_code == 200
    assert {
        "title": "Moby Dick",
        "author": "Herman Melville"
    } == retrieve.json()


def test_delete_book(base_server_url: str):
    resp = requests.post(base_server_url + "/books", json={
        "title": "Moby Dick",
        "author": "Herman Melville"
    })

    uuid_str = resp.headers.get("Location").split("/books/")[-1]

    delete_resp = requests.delete(base_server_url + "/books/" + uuid_str)

    assert delete_resp.status_code == 204

    retrieve = requests.get(base_server_url + "/books/" + uuid_str)

    assert retrieve.status_code == 404
