import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from mf6.home.models import SuscriptorType

Suscriptor_dict = {
    'category': ['Freemium', 'Hatari', 'HatariPlus'],
    'n_projects': [3, 10, 20],
    'ref_stages': [3, 5, 7],
    'n_cells': [1000, 5000, 10000],
    'n_layers': [5, 10, 20],
    'n_periods': [5, 10, 20]
}

for i in range(len(Suscriptor_dict['category'])):
    suscriptor_type = SuscriptorType(
        category=Suscriptor_dict['category'][i],
        n_projects=Suscriptor_dict['n_projects'][i],
        ref_stages=Suscriptor_dict['ref_stages'][i],
        n_cells=Suscriptor_dict['n_cells'][i],
        n_layers=Suscriptor_dict['n_layers'][i],
        n_periods=Suscriptor_dict['n_periods'][i]
    )
    suscriptor_type.save()

from allauth.socialaccount.models import SocialApp

demo_dict = {
	'provider' : 'Keycloak',
	'name' : 'demo',
	'client_id' : 'djangoTupacCloud',
	'secret_key' : 'xrmqy5y9fESkt4xYNZpmB140m4IHHxLq',
	'key' : 'eyJhbGciOiJIUsInR5cCIgOiAiSldUIiwia2lkIiA6ICI1Y2M4MDZlNS0wM2E5LTQ4ODItOWQzYi04ODg1OWViZTMwZjAifQ.eyJleHAiOjAsImlhdCI6MTY3MDM1NzQzMCwianRpIjoiODUwNjJmYjYtNTkzNS00OTVmLTk5M2EtMDFhNWYzI1NiI2Yjky'
}

social_app = SocialApp(
    provider=demo_dict['provider'],
    name=demo_dict['name'],
    client_id=demo_dict['client_id'],
    secret=demo_dict['secret_key'],
    key=demo_dict['key']
)
social_app.save()