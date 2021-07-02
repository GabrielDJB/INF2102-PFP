# Installation
In order to install the necessary dependencies, users must first install a _Python_ distribution from https://www.python.org/downloads/. Once installed, users can use `pip` to install all required libraries based on the `requirements.txt` file. You can do so through the following command:

```Batch
pip install -r requirements.txt
```

# Execution
Once all dependencies are installed, the back-end server can be run via the `deploy.bat` file. It runs the following commands:

```Batch
CALL back-env\Scripts\activate.bat
set FLASK_APP=app.py
flask run
```

# Testing
As well as running the back-end development server, users can also run the automated testing via the `test.bat` file. It runs the following commands:

```Batch
CALL back-env\Scripts\activate.bat
pytest
cmd /k
```
This generates a report for the automated testing procedure. There is no need to run the development server separately, the testing script instantiates one on its own.
