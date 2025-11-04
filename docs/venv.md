# Conofigure Python Project with UV:

1. Install UV
    ```sh
    # manually:
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # with brew:
    brew install uv
    ```

2. Install python 3.14
    ```sh
    uv python install 3.14

    # if this needs to be default version in the system:
    uv python install 3.14 --default
    ```

3. Activate Venv by navigate to the project folder and running commands:
    ```sh
    uv venv
    source .venv/bin/activate
    ```

4. Bootstrap pip into the env:
    ```sh
    python -m ensurepip
    ```

5. Install packages:
    ```sh
    uv pip install <package name>

    # or with requirements file:
    uv pip install -r requirements.txt
    ```