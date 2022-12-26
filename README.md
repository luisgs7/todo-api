# Django-step-by-step

To initialize the project, run the commands below:

#### Create the virtual environment
```
python3 -m venv venv
```

#### Create an .env file from .env.example
```
SECRET_KEY="secret_key"
DEBUG=True
ALLOWED_HOSTS= ["*", "127.0.0.1"]
```

#### install the dependencies
```
pip install -r requirements.txt
```

### Initialize the development Django server
```
python manage.py runserver
```

