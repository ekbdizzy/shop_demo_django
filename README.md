## Shop Demo on Django 3.0

### Description
It's a simple shop demo on Django with main page, category view and product detail view, built on Bootstrap4.

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
For global settings is used django-environ.<br>
Sample:
~~~
DEBUG=True
SECRET_KEY=c3ohcmsp=6%g#mz-iz6jl_=4wbhlpzr%6d0ag1+(&y=#q20%z_
ALLOWED_HOSTS=localhost,192.168.0.1
DATABASE_URL=sqlite:////Users/mak/PycharmProjects/django_demo_shop/db.sqlite3
INTERNAL_IPS=localhost,192.168.0.1,127.0.0.1
~~~
More info: https://django-environ.readthedocs.io