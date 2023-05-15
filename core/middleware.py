import requests
from allauth.socialaccount.models import SocialToken

class KeycloakIDTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated and id_token is in request.GET
        if request.user.is_authenticated :
            # Store the id_token in the user's session
            #request.session['id_token'] = request.GET.get('id_token')
            social_account = request.user.socialaccount_set.last()
            token = SocialToken.objects.filter(account=social_account,app = 1).last() 


        response = self.get_response(request)
        return response