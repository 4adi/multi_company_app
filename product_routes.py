
from flask import Blueprint, request, jsonify, g
from flask_jwt_extended import jwt_required

product_bp = Blueprint("products", __name__)

@product_bp.post("/add-product")
@jwt_required()
def add_product():
    data = request.json
    product = {
        "name": data["name"],
        "description": data["description"],
        "image_url": data.get("image_url")
    }

    g.db.products.insert_one(product)

    return jsonify({"msg": "Product added successfully!"})
