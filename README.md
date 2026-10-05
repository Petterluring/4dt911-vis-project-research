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


## Access to Remote Services

The research part of the project depend on a remote virtual machine hosted on Linnaeus University's (LNU) Computer Science (CS) cloud. The machine is accessible at [cu0089.camp.lnu.se](https://cu0089.camp.lnu.se/).

Access to the virtual machine requires a connection to the EDU VPN when accessing it from outside the campus network. See the [VPN instructions](https://www.lnu.se/mot-linneuniversitetet/aktuellt/nyheter/2025/nytt-student-vpn/) for information on configuring the VPN connection.

The project also requires access to the `4dt911-resources` folder, which contains the credentials necessary to connect to the remote services. Contact a project member to obtain access to this folder. The folder contains configuration files with the credentials required to access the two services on which the research depends on:

* **MLflow** — used for machine learning experiment tracking and model management.
* **PostgreSQL** — used as the project's database.

Once you have obtained the folder, place it in your home directory. Make sure that the `HOME` environment variable is correctly configured on your machine. You can verify this by running:

```bash
echo $HOME
```

If configured correctly, the command should print the path to your home directory.

Once everything is set up, you can test the connections to the MLflow and PostgreSQL servers by running the `connection_test.ipynb` notebooks located in `notebooks/demos/mlflow/` and `notebooks/demos/postgresql/`, respectively.


## Repository layout

```text
src/                       # Reusable code that can be used on notebooks
notebooks/                 # Contains all notebooks for ml research
pyproject.toml             # Project metadata and dependencies
poetry.lock                # Reproducible dependency lock file
```

## Security and data handling

- Never commit `~/4dt911-resources`, passwords, access tokens, or private keys.
- Never commit private or institution-provided certificates unless explicitly
  approved by LNU and the project maintainers.
- Avoid placing sensitive data in notebooks, notebook outputs, or experiment
  parameters.
