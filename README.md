# Shop Demo on Django 3.0

### Description
It's a simple shop demo on Django.

### Dependencies
~~~~
pip install -r requirements.txt
~~~~

### Create and fill database
~~~~
python manage.py makemigrations
python manage.py migrate
python manage.py fill_db  # create models for categories and products using factory_boy 
~~~~

### Django environment setting
For global settings is used django-environ<br>
Settings file is **django_demo_shop/.env**<br>
More info: https://django-environ.readthedocs.io