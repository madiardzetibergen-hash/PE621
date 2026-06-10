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


# --------------SET МНОЖЕСТВА--------------

# numbers = {1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9}
# print(numbers[2])

# data = {{1,2}, {3,4}}

# numbers = {1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9}
# for i in numbers:
#     if i == 2:
#         print(i)

# numbers = [1,2,2,2,3,4,5,5,6,7,8,9,9]
# unique_numbers = set(numbers)
# new_numbers = list(unique_numbers)
# print(new_numbers)

# skills = {"Python", "HTML"}
# skills.add("CSS")
# print(skills)

# update()
# skills = {"Python", "HTML"}
# skills.update(["CSS", "JS", "REACT"])
# print(skills)

# remove()
# skills = {"Python", "HTML"}
# skills.remove("qwerty")
# print(skills)

# discard()
# skills = {"Python", "HTML"}
# skills.discard("qwerty")
# print(skills)

# numbers = {1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9}
# item = numbers.pop()
# print(item)
# print(numbers)

# clear()

# Операции с множеством
group_a = {1,2,3,4,8}
group_b = {4,5,6,7,8}
# result = group_a & group_b
# print(result)
result = group_a | group_b
result = group_a.union(group_b)
print(result) 