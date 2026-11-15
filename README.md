# unit-converter

Native Python3.11–3.13 application; intended acceptance runtime3.12.
Install `python -m pip install -r requirements.txt` in an isolated environment.
Run `python -m pytest`. Start `uvicorn unit_converter.app:app --host 0.0.0.0 --port 8201`.



POST /convert {kind:temperature|distance,value,source,target}; units C/F or m/km, output decimal string with6 digits.
Tests are source-native development checks. Tests exercise actual in-process FastAPI routing and domain rules.
AI-assisted researcher-created source; no deployment files or runtime credentials.
