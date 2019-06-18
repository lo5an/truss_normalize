# truss_normalize - processes sample csvs. 

This script will perform assorted normalization on a particular data csv, as specified at 
https://github.com/trussworks/truss-interview

## Requirements

This script requires Python 3, and has been tested against 3.6. Additionally, it makes use
of `pytz` and the included tests require `pytest`.

## Install and Run

My workflow for running the script in a python virtual environment looks something like:

```
git clone git@github.com:lo5an/truss_normalize.git
cd truss_normalize
python3 -m venv ./env
. env/bin/activa 
pip install -r requirements.txt
python3 truss_normalize.py  < ~/Downloads/sample.csv  > clean.csv
```


