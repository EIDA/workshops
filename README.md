# Introduction
txt

## Quick start guide

### Run using Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/EIDA/workshops/HEAD?filepath=notebooks%2F)

### Run on local machine

#### Run with Python venv

1. Clone the repository and go to its root directory
1. Create the virtual environment:

    ```bash
    python3 -m venv env
    ```

1. Activate the virtual environment:

    ```bash
    source env/bin/activate
    ```

1. Install the dependencies:

    ```bash
    pip install jupyter==1.0.0
    pip install -r requirements.txt
    ```

1. Run the server:

    ```bash
    jupyter notebook notebooks/
    ```

#### Run with conda (preferred)

1. Clone the repository and go to its root directory
1. Create the conda environment:

    ```bash
    conda create --prefix ./.env python=3.9
    ```

1. Activate the conda environment:

    ```bash
    conda activate ./.env
    ```

1. Install the dependencies:

    ```bash
    conda install -c conda-forge jupyter
    conda install -c conda-forge obspy
    conda install -c conda-forge cartopy
    ```

1. Run the server:

    ```bash
    jupyter notebook notebooks/
    ```
