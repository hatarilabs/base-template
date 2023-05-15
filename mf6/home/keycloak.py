import requests

# Keycloak server information
#keycloak_url = 'https://accounts.hatarilabs.com/realms/demo/protocol/openid-connect/auth'
keycloak_url = 'https://accounts.hatarilabs.com/realms/demo/protocol/openid-connect/token'
client_id = 'shopHatarilabs'
client_secret = 'yRTNItA9IWBGx9uzsTjQ6OBGgCuDvH6B'

#client_id = 'djangoTupacCloud'
#client_secret = 'xrmqy5y9fESkt4xYNZpmB140m4IHHxLq'

#client_id = 'admin-cli'


# User credentials
username = 'ingjosezr@gmail.com'
password = 'jose'

# Request a token using the Resource Owner Password Credentials Grant flow
payload = {
    'grant_type': 'password',
    'client_id': client_id,
    'client_secret': client_secret,
    'username': username,
    'password': password,
}


response = requests.post(keycloak_url, data=payload)

# Check if the request was successful
if response.status_code == 200:
     # Extract the token from the response
    access_token = response.json()['access_token']
    print(f'Token: {access_token}')
else:
    print(f'Error: {response.status_code} - {response.reason}')




url = "https://accounts.hatarilabs.com/admin/realms/demo"

headers = {"Authorization": f"Bearer {access_token}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Handle successful response
    print(response.json())
else:
    # Handle error response
    print("Error:", response.status_code, response.text)