import logging
import time
from multiprocessing import Process

import pytest
import requests

from src.server import app


def server_instance(server_host, server_port):
    logging.basicConfig(filename="test_server_flask.log", filemode="w")
    app.run(server_host, server_port)


@pytest.fixture(scope="session")
def base_server_url():
    logging.info("Beginning server setup")
    host = "0.0.0.0"
    port = 5000

    process = Process(None, target=server_instance, args=(host, port), daemon=True)
    logging.info("starting server process")
    process.start()

    url = f"http://{host}:{port}"

    flask_running = False

    while not flask_running:
        if not process.is_alive():
            logging.info("Process did not survive.")
            pytest.fail("Process did not survive.")
        try:
            requests.get(url)
            flask_running = True
        except requests.ConnectionError:
            logging.info("Waiting for server connection")
            time.sleep(0.1)

    yield url

    logging.info("killing server process")
    process.kill()
    process.join()
