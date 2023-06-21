# base-template

python .\manage.py migrate

python manage.py makemigrations home

python .\manage.py migrate

python .\fill_data.py

python manage.py createsuperuser

python manage.py shell

from django.contrib.sites.models import Site

Site.objects.create(domain='localhost', name='localhost')

python .\manage.py runserver 0.0.0.0:7777
