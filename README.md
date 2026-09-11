# 4DT911 Visualization Analytics — ML Research

This repository contains the machine-learning research code for the visualization
analytics project in the course **4DT911**. It is used to experiment
with data preparation, model training, and evaluation.

Trained models and their related metadata are logged to and stored in **MLflow**.
The project's backend service uses the models and MLflow tracking information
produced by this repository, so experiments should be reproducible and clearly
named.

## Requirements

- Python 3.14 or newer
- [Poetry](https://python-poetry.org/docs/#installation) 2.x
- Access to the project's MLflow tracking server
- The following MLflow connection resources:
  - An environment file containing the MLflow server URL, username, and password
  - The SSL certificate issued by LNU (Linnaeus University) for the MLflow server

Do not commit credentials or the certificate to this repository. Store them in
your user directory as described below.

## Initialize and install

Clone the repository and enter its directory:

```bash
git clone https://github.com/Petterluring/4dt911-vis-project-research.git
cd 4dt911-vis-project-research
```

Make sure that poetry creates its virtual enviroments inside the project in a .venv directory:
```bash
poetry config virtualenvs.in-project true
```

Install the project and its dependencies with Poetry:
```bash
poetry install
```

Alternatively you can install with the developer dependencies which includes linting tools.
```bash
poetry install --extras dev
```

Poetry will create (or reuse) a virtual environment and install the locked
dependencies from `poetry.lock`.

## Running notebooks
It is assumed that the user knows how to run .ipynb notebooks using IDEs such as VS code.


## MLflow configuration

The MLflow helper in `src/mlflow_utils/mlflow_config.py` expects the following
files in `~/.mlflow-data/`:

```text
~/.mlflow-data/
├── .env
└── SSL_certificate.crt
```

Create the directory:

```bash
mkdir -p ~/.mlflow-data
```

### Environment file

Create `~/.mlflow-data/.env` with the credentials supplied for the project's
MLflow server:

```dotenv
MLFLOW_TRACKING_URI=https://<mlflow-server-url>
MLFLOW_TRACKING_USERNAME=<mlflow-username>
MLFLOW_TRACKING_PASSWORD=<mlflow-password>
```
The server must be communicated over https.

Keep this file private and restrict its permissions where supported:

```bash
chmod 600 ~/.mlflow-data/.env
```

### LNU SSL certificate

Obtain the CA/server certificate from the LNU university from the project's MLflow administrators. Save the certificate in PEM/CRT format as:

```text
~/.mlflow-data/SSL_certificate.crt
```

The MLflow helper sets `MLFLOW_TRACKING_SERVER_CERT_PATH` to this file before
connecting. This lets the MLflow client trust the HTTPS certificate presented by
the server. The file must exist and be readable; otherwise configuration loading
fails before a connection is attempted.

If the certificate or environment file is stored elsewhere, pass the paths
explicitly when loading the configuration:

```python
from mlflow_utils import load_config

load_config(
    env_path="/path/to/.env",
    certificate_path="/path/to/SSL_certificate.crt",
)
```

## Repository layout

```text
src/                       # Reusable code that can be used on notebooks
notebooks/                 # Contains all notebooks for ml research
pyproject.toml             # Project metadata and dependencies
poetry.lock                # Reproducible dependency lock file
```

## Security and data handling

- Never commit `~/.mlflow-data/.env`, passwords, access tokens, or private keys.
- Never commit private or institution-provided certificates unless explicitly
  approved by LNU and the project maintainers.
- Use separate MLflow credentials for development and production/backend
  services where possible.
- Avoid placing sensitive data in notebooks, notebook outputs, or experiment
  parameters.
