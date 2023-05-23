"""
Scenario:
    You own an e-commerce marketplace site. Several partners sell their products on your site.
    Like amazon.com. The partners update their list of products and prices daily. They send you the
    product information in one of several ways (API, FTP, Email, ...).

    You have received the products information and created a list as provided below.
    Variable 'products' is the list of products you have received.


Exercise 1:
    - Iterate the products list and print the name of all products that have price greater than 25.

Exercise 2:
    - Print the name and price of products that are on sale.

Exercise 3:
    - Create a list of products (product names) that are on sale but do not have a sale price.
    - If a product is on sale but does not have sale price, you need to let the partner know. So the list of
        products you generate will be shared with the partner. But for purpose of this exercise, just print the list
        of sale products without sale price that you created.
"""

products = [
    {'id': 1, 'name': 't-shirt', 'price': 12.99, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 2, 'name': 'shoes', 'price': 22.45, 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 3, 'name': 'dress-shirt', 'price': 43.00, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 4, 'name': 'socks', 'price': 14.99, 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': 7.99},
    {'id': 5, 'name': 'trousers', 'price': 32.50, 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 6, 'name': 'jacket', 'price': 150.00, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
]

print("Solution for ex 1.")

for i in products:
    if i['price'] > 25:
        print(i['name'])

print("#========================================")
print("Solution for ex 2.")

for i in products:
    # if i['is_on_sale'] == True:
    if i['is_on_sale']: # Pythonic way (Truthiness)
        print(i['name'])
        print(i['price'])


print("#========================================")
print("Solution for ex 3.")

no_sale_price_list = []
for i in products:
    # if i['is_on_sale'] == True and i['sale_price'] == None:
    if i['is_on_sale'] and not i['sale_price']: # same statement as above
        no_sale_price_list.append(i['name'])
print(no_sale_price_list)










