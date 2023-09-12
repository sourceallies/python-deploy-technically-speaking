# Simple Python/Flask/NGINX Server Boilerplate

## Initial Setup

- Some container running software. Ex:

  - [Docker Desktop](https://www.docker.com/products/docker-desktop/)
  - [Rancher Desktop](https://rancherdesktop.io/)
  - [Minikube](https://minikube.sigs.k8s.io/docs/commands/docker-env/)
  - [Podman](https://podman.io/)
  - [Colima (Mac/Linux Only)](https://github.com/abiosoft/colima)

- Python 3.11 install. Ex:

  - [Direct installation from Python.org](https://www.python.org/downloads/)

    - Recommendation: Use a virtual environment when possibly to not pollute your global python install when using a direct python installation:

      ```shell
      # this creates a new virtual env
      # should only need to do this once
      $ python3 -m venv venv
      ```

      ```shell
      # activate the environment so that the python command points to the executable in venv/bin
      $ source venv/bin/activate
      ```

  - [Using Poetry](https://python-poetry.org/)
  - [Python 3 Docker Image](https://hub.docker.com/_/python/)

## Running Tests

- Direct installation (assuming venv activated):
  ```shell
  (venv) $ pytest
  ```
- Poetry
  ```shell
  poetry run pytest
  ```
