# conofigure python project with UV:

Install UV
```sh
# manually:
curl -LsSf https://astral.sh/uv/install.sh | sh

# with brew:
brew install uv
```

install python 3.14
```sh
uv python install 3.14

# if this needs to be default version in the system:
uv python install 3.14 --default
```

navigate to the project folder and activate venv:
```sh
uv venv
source .venv/bin/activate
```

add pip to the env:
```sh
python -m ensurepip
```

install packages:
```sh
uv pip install <package name>

# or with requirements file:
uv pip install -r requirements.txt
```