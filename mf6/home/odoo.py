import requests
import json

# Authenticate to the API
session = requests.Session()
url = 'https://shop.hatarilabs.com/web/session/authenticate'


params = {'jsonrpc': '2.0','method' : 'call','params': {'context':{},'login': 'saulmontoya@hatarilabs.com', 'password': 'Wkgidahatari_1', 'db': 'postgresOdoo'}}
#params = {'jsonrpc': '2.0','method' : 'call','params': {'context':{},'login': 'ingjosezr@gmail.com', 'password': 'jose', 'db': 'postgresOdoo'}}


headers = {'Content-Type': 'application/json'}
response = session.post(url, headers=headers, data=json.dumps(params))

# Check if the authentication was successful
if response.status_code != 200:
    raise ValueError('Authentication failed')
else:
	print("you are in")

session_id = response.cookies["session_id"]

#print(response.text)


# Call an API method using the new session ID
headers = {
    'Content-Type': 'application/json',
    'Cookie': 'session_id=' + session_id
}
data = {
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'model': 'res.partner',
        'method': 'search_read',
        'args': [[('is_company', '=', True)], ['name', 'email', 'phone']],
        'kwargs': {}
    }
}
response = session.post('https://shop.hatarilabs.com/web/dataset/call_kw', headers=headers, json=data)

# Print the response
print(json.dumps(response.json(), indent=4))
results = response.json()['result'][0]


user_id = results['id']
print(user_id)

# retrieve all purchases made by the user
data = {"jsonrpc": "2.0", "method": "call", "params": {"session_id": session_id, "model": "purchase.order", "method": "search_read", "args": [[('user_id', '=', user_id)]], "kwargs": {"fields": ['name', 'amount_total', 'date_order']}}, "id": None}
response = requests.post('https://shop.hatarilabs.com/web/dataset/call_kw', headers=headers, json=data, cookies={'session_id': session_id})
purchases = response.json()#['result']

print(purchases)

# print out the purchases
# for purchase in purchases:
#     print(purchase['name'], purchase['amount_total'], purchase['date_order'])