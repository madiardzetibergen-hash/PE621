# user = {
#     "id": 1,
#     "name": "Azamat",
#     "grade": 85
# }
# print(user)
# print(user["grade"])

# user = {
#     "id":1,
#     "name":"Amina",
#     "email": "amina@gmail.com",
#     "is_active": True
# }

# settings = {
#     "theme": "dark",
#     "lang": "english",
#     "notification": True
# }

products = {
    "id": 101,
    "title": "Laptop",
    "price": 350000,
    "in_stock": True
}
# products["discount"] = 40
# products["id"] = 597
# del products["price"]
# products.pop("price")
# products.popitem()
# print(products.get("title", "Title не существует"))
# print(products.get("email", "Email не существует"))
# print(products)
# print(products.keys())
# print(products.values())

# ----------Циклы по dict-----------
for i in products:
    print(i)
print()
for i in products.keys():
    print(i)
print()
for i in products.values():
    print(i)
print()
for key,value in products.items():
    print(key, value)