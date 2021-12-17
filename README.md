#### Maakay Twitter/ Discord Bot Template

Feel free to use this bot to getting started on integrating TNBC to twitter/ discord/ telegram bot.

#### Development Guide

- Clone the repo

- Activate the virtual environment. https://docs.python.org/3/library/venv.html

- Install the requirements using `pip install -r requirements.txt`

- Set environment variables:
```shell
BOT_ACCOUNT_NUMBER (TNBC Account Number for receiving payment)
SIGNING_KEY (TNBC Signing Key handling payments)
CHECK_TNBC_CONFIRMATION (True or False)
BANK_IP (Bank IP to handle TNBC payment)
KEYSIGN_BANK_IP (Keysign Bank IP to check cross bank confirmations)

DJANGO_SETTINGS_MODULE (config.settings.development or config.settings.production)
SECRET_KEY (Django Secret Key)

ACCESS_TOKEN
ACCESS_TOKEN_SECRET
API_KEY
API_KEY_SECRET

# For production
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_HOST
POSTGRES_PORT
```

##### To run the bot:

- Use command `python bot.py`

##### To run django server

- Use `python manage.py migrate` to create database.

- Create superuser with the command `python manage.py createsuperuser`.

- Run the server with `python manage.py runserver`.

Happy building!!
