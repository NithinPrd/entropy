# Setup

## Prerequisites
Make sure you have django and python3 installed. I will try to containerize the project in the coming future, but it'll be a bit hacky to run till then.

Run the following commands:
```
cd voting

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
```

## How to run

```
python manage.py runserver
```