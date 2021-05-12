:: Activating virtual environment
CALL back-env\Scripts\activate.bat

:: Deploying flask server
set FLASK_APP=app.py
flask run