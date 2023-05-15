from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from allauth.account.views import LogoutView
from allauth.socialaccount import providers
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from django.urls import reverse_lazy


#import jwt
#from jwt.algorithms import RSAAlgorithm

#import logging

#logger = logging.getLogger(__name__)
#from allauth.socialaccount.signals import pre_social_login
#from django.dispatch import receiver

# @receiver(pre_social_login)
# def get_id_token(request, sociallogin, **kwargs):
#     id_token = sociallogin.token#.id_token
#     your_public_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwI9mqttgYCBRFPzFwfNek/0zRjVlpuZxl+srnjzVmAdqvwBS76AHpB3Oa6J4TWGDStXcvJtkX2mUk2A9SVpCiAaI1KWzvSgTRQc+7nRxmTRRDBIHGArw1RDHuLhhusjsnRFvnQoycqIWwDYqYH9TuGPiYmROobIEJtfp05kT9t5VBWHpUSJGJmJsFqI2ThbFykPIoY3/OOqFKwiFYRSdrAvXq9s8IUfbofTuV5pVrRJAPwl3lVVlVrOqbV4B0h70mKscOcfJZtIeFgCui2o/la/xyEbgFSnlCEacyOCEgnFvbjvTFNPXqRMzmLXhENjRhIJCw4nB4QG2HKpfQEt9HwIDAQAB"
#     public_key = f"-----BEGIN PUBLIC KEY-----\n{your_public_key}\n-----END PUBLIC KEY-----"
#     client_id = 'djangoTupacCloud'
#     #print('hola')
#     fields = SocialToken._meta.get_fields()

#     print(request.session.get('id_token'))

#     for i,field in enumerate(fields):
#         field_name = field.name
#         field_value = getattr(id_token, field_name)
#         print("campo "+str(i))
#         print(f"{field_name}: {field_value}")
    

def index(request):
    context = {}
    html_template = loader.get_template('home/landing.html')
    return HttpResponse(html_template.render(context, request))


class KeycloakLogoutView(LogoutView):    

    redirect_field_name = 'https://tupaccloud.hatarilabs.com/'

    def get_redirect_url(self):
        try:
            social_account = self.request.user.socialaccount_set.last()
            print(social_account.extra_data.get('id_token'))                
            social_token = SocialToken.objects.filter(account=social_account,app = 1).last() 
            id_token = social_token.token#token_secret            
            index_page_url = self.request.build_absolute_uri(reverse_lazy('home'))
            keycloak_base_url = 'https://accounts.hatarilabs.com/realms/demo/protocol/openid-connect/logout'
            logout_url = f"{keycloak_base_url}?post_logout_redirect_uri={index_page_url}&id_token={id_token}&id_token_hint={id_token}"
            logout_url = f"{keycloak_base_url}?"
            return logout_url
        except OAuth2Error as e:
            print(e)
            return super().get_redirect_url()
        except SocialToken.DoesNotExist:
            return super().get_redirect_url()