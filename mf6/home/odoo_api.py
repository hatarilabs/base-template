import xmlrpc.client
info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
url, db, username, password = info['host'], info['database'], info['user'], info['password']

print(db)


# Odoo API information
url = 'https://shop.hatarilabs.com/'
db = 'postgresOdoo'
username = 'admin'
password = 'admin'

# Connect to the Odoo server
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

# Connect to the Odoo API
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))


# Search for the user by email or username
email = 'ingjosezr@gmail.com'  # Replace with the user's email or username
user_ids = models.execute_kw(db, uid, password,
    'res.users', 'search', [[('login', '=', email)]])

# Print the user ID
if user_ids:
    user_id = user_ids[0]
    print(f"User ID: {user_id}")
else:
    print("User not found.")


# # Search for the user's sale orders
# user_id = 1  # Replace with the user's ID
order_ids = models.execute_kw(db, uid, password,
    'sale.order', 'search', [[('partner_id', '=', user_id)]])

print(order_ids)
# Get the list of products purchased in each sale order
product_ids = []
for order_id in order_ids:
    order = models.execute_kw(db, uid, password,
        'sale.order', 'read', [order_id], {'fields': ['id']})    
    for line in order[0]['id']:
        product_ids.append(line['product_id'][0])


# Get the product names
products = models.execute_kw(db, uid, password,
    'product.product', 'read', [product_ids], {'fields': ['name']})

# Print the list of product names
for product in products:
    print(product['name'])


"""
# Get the list of model names
model_names = models.execute_kw(db, uid, password,
                                'ir.model', 'search_read',
                                [[]], {'fields': ['model']})

# Print the model names
for model in model_names:
    print(model['model'])
"""
product_names = models.execute_kw(db, uid, password,
                                'slide.channel', 'search_read',
                                [[]], {'fields': ['display_name','enroll','enroll_group_ids','activity_user_id']})

# Print the model names
for product in product_names:
    print(product)


product_names = models.execute_kw(db, uid, password,
                                'sale.order', 'search_read',
                                [[]], {'fields': []})

# Print the model names
for product in product_names:
    print(product)


product_names = models.execute_kw(db, uid, password,
                                'subscription.package', 'search_read',
                                [[]], {'fields': []})

# Print the model names
for product in product_names:
    print(product)
