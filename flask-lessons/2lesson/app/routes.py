from flask import Blueprint,jsonify,request

from app.data import products
from app.data import get_next_id

products_bp = Blueprint(
    "products",
    __name__
)

def find_product(product_id):
    return next(
        (
            product
            for product in products
            if product["id"] == product_id
        ),
        None
    )

# "GET READ"

@products_bp.route("/")
def home():
    return "Главная страница"

@products_bp.get("/products")
def get_products():
    return jsonify({
        "count": len(products),
        "products": products
    }), 200

@products_bp.get("/products/<int:product_id>")
def get_product_by_id(product_id):
    product = find_product(product_id)

    if product is None:
        return jsonify({
            "error": "Товар не найден"
        }),404
    
    return jsonify(product), 200

# "POST CREATE"

@products_bp.post("/products")
def create_product():
    data = request.get_json(silent = True)

    if data is None:
        return jsonify({
            "error": "Необходимо отправить JSON"
        }),400
    
    if "name" not in data:
        return jsonify({
            "error": "Поле name обязательна"
        }),400
    
    if "price" not in data:
        return jsonify({
            "error": "Поле price обязательна"
        }),400
    
    if "quantity" not in data:
        return jsonify({
            "error": "Поле quantity обязательна"
        }),400
    
    name = data["name"]
    price = data["price"]
    quantity = data["quantity"]

    if not isinstance(name,str) or name.strip() == "":
        return jsonify({
            "error": "name должен быть непустой строкой"
        }),400
    
    if not isinstance(price,(int,float)) or price < 0:
        return jsonify({
            "error": "price должен быть полжительным числом"
        }),400 
    
    if not isinstance (quantity,(int,float)) or price < 0:
        return jsonify({
            "error": "количество должно быть полжительным числом"
        }),400
    
    new_product = {
        "id": get_next_id(),
        "name": name.strip(),
        "price": price,
        "quantity": quantity
    }
    products.append(new_product)
    
    return jsonify({
        "message": "Товар успешно создан",
        "product": new_product
    }), 201

@products_bp.put("/products/<int:product_id>")
def update_product(product_id):
    product = find_product(product_id)

    if product is None:
        return jsonify({
            "error":"Товар не найден"
        }),404
    
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            "error": "Необходимо отправить JSON"
        }), 400
    
    requied_fields = [
        "name",
        "price",
        "quantity"
    ]

    missing_fields = [
        field
        for field in requied_fields
        if field not in data 
    ]

    if len(missing_fields) > 0:
        return jsonify({
            "error": "Для Put необходимо передать все поля",
            "missing": missing_fields
        }), 400
    
    name = data["name"]
    price = data["price"]
    quantity = data["quantity"]

    if not isinstance(name,str) or name.strip() == "":
        return jsonify({
            "error": "name должен быть непустой строкой"
        }),400
    
    if not isinstance(price,(int,float)) or price < 0:
        return jsonify({
            "error": "price должен быть полжительным числом"
        }),400 
    
    if not isinstance (quantity,(int,float)) or quantity < 0:
        return jsonify({
            "error": "количество должно быть полжительным числом"
        }),400
    
    product["name"] = name.strip()
    product["price"] = price
    product["quantity"] = quantity
    
    return jsonify({
        "message": "Товар успешно обновлен",
        "product": product
    }),200
    
@products_bp.patch("/products/<int:product_id>")
def patch_product(product_id):
    product = find_product(product_id)

    data = request.get_json(silent=True)

    if product is None:
        return jsonify({
            "error": "Необходимо отправить JSON"
        }),400
    
    allowed_fields =[
        "name",
        "price",
        "quantity"
    ]

    received_allowed_fields = [
        field
        for field in allowed_fields
        if field in data
    ]

    if len(received_allowed_fields) == 0:
        return jsonify({
            "error": "Необходимо передать хотябы одно поле",
            "allowed_fields": allowed_fields
        }),400
    
    if "name" in data:
        if not isinstance(data["name"],str) or data["name"].strip() == "":
            return jsonify({
                "error": "name должен быть не пустой строкой"
            }),400
        product["name"] = data["name"].strip()

    if "price" in data:
        if not isinstance(data["price"], (int,float)) or data["price"] < 0:
            return jsonify({
                "error": "price должен быть положительным числом"
            }),400
        product["price"] = data["price"]
    if "quantity" in data:
        if not isinstance(data["quantity"], (int,float)) or data["quantity"] < 0:
            return jsonify({
                "error": "quantity должен быть положительным числом"
            }),400
        product["quantity"] = data["quantity"]

    return jsonify({
        "message": "Товар частично обновлен",
        "product": product   
    })

@products_bp.delete("/products/<int:product_id>")
def delete_product(product_id):
    product = find_product(product_id)

    if product is None:
        return jsonify({
            "error": "Товар не найден"
        }), 404
    
    products.remove(product)

    return jsonify({
        "message":"Товар успешно удален",
        "product":product
    }),200
        
    


