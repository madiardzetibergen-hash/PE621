products = [
    {"id": 1, "name": "Laptop", "price": 350000, "quantity": 5},
    {"id": 2, "name": "Smartphone", "price": 280000, "quantity": 12},
    {"id": 3, "name": "Wireless Headphones", "price": 45000, "quantity": 25},
    {"id": 4, "name": "Smartwatch", "price": 85000, "quantity": 8},
    {"id": 5, "name": "27\" Monitor", "price": 120000, "quantity": 7},
    {"id": 6, "name": "Mechanical Keyboard", "price": 32000, "quantity": 15},
    {"id": 7, "name": "Gaming Mouse", "price": 18000, "quantity": 30},
    {"id": 8, "name": "External SSD 1TB", "price": 55000, "quantity": 10},
    {"id": 9, "name": "Tablet", "price": 190000, "quantity": 6},
    {"id": 10, "name": "Full HD Webcam", "price": 24000, "quantity": 18},
]
def get_next_id():
    if len(products) == 0:
        return 1
    
    max_id = max(product["id"] for product in products)
    return max_id + 1
    