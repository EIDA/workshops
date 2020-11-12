# Introduction
This repository contains Jupyter notebooks presenting 2 very different approaches
to downloading seismic waveforms and station metadata from the ORFEUS Data Center:

1. `notebooks/webdc3` presents a typical use case of finding a seismic event in the area of the Groningen gas field, selecting stations from its surroundings, downloading the event waveforms and station metadata using [WebDC3](http://orfeus-eu.org/webdc3/) web application hosted at the [ORFEUS Data Center](https://www.orfeus-eu.org/data/odc)
1. `notebooks/webservices-obspy` is a more advanced workflow example focused on the [ObsPy](https://github.com/obspy/obspy) Python library and usage of the web services provided by the [ORFEUS Data Center](https://www.orfeus-eu.org/data/odc):
    1. [FDSNWS-Dataselect](http://orfeus-eu.org/fdsnws/dataselect/1/) (raw waveforms)
    1. [FDSNWS-Station](http://orfeus-eu.org/fdsnws/station/1/) (station metadata)
    1. [EIDAWS-WFCatalog](http://www.orfeus-eu.org/eidaws/wfcatalog/1/) (waveform quality metrics)

# Quick start guide

## Run using Binder
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/EPOS-NL/eposnl-orfeus-notebooks/HEAD?filepath=notebooks%2F)

## Run on local machine
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

# References
|Description|URL|
|-|-|
|EPOS-NL|https://epos-nl.nl|
|ORFEUS Data Center|https://www.orfeus-eu.org/data/odc|
|ObsPy|https://github.com/obspy/obspy|
|Seismo-Live (more notebooks with usage examples)|http://seismo-live.org|
