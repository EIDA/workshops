# Introduction
txt

# Quick start guide

## Run using Binder
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/EIDA/workshops/HEAD?filepath=notebooks%2F)

## Run on local machine
1. Clone the repository and go to its root directory
1. Create the virtual environment:
    ```
    $ python3 -m venv env
    ```
1. Activate the virtual environment:
    ```
    $ source env/bin/activate
    ```
1. Install the dependencies:
    ```
    (env) $ pip install jupyter==1.0.0
    (env) $ pip install -r requirements.txt
    ```
1. Run the server:
    ```
    (env) $ jupyter notebook notebooks/
    ```
