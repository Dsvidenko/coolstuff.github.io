# PythonAnywhere Starter

This repository contains a simple Flask application that can be deployed on [PythonAnywhere](https://www.pythonanywhere.com/).

The app serves a greeting page at `/` and shows a sample matplotlib plot at `/plot`.

## Running locally

1. Install the dependencies:

```bash
pip install flask matplotlib
```

2. Start the server:

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## Deploying on PythonAnywhere

1. Create a new **Web App** on PythonAnywhere.
2. Set the `WSGI configuration file` to point to this application's directory and import the `app` object from `app.py`.
3. Reload the web app to see the changes.

