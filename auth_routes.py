# When user logs in:

# Verify username & password (dummy example for now)

# Identify company

# Generate JWT token containing company_name & user_id


from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
auth_bp = Blueprint("auth", __name__)

# Temporary hardcoded users (use MongoDB in real projects)
USERS = {
    "aadil": {"password": "1234", "company": "companyA"},
    "rahul": {"password": "abcd", "company": "companyB"},
}

@auth_bp.post("/login")
def login():
    data = request.json
    username = data["username"]
    password = data["password"]

    if username not in USERS or USERS[username]["password"] != password:
        return jsonify({"msg": "Invalid credentials"}), 401

    user = USERS[username]
    token = create_access_token(identity=username, additional_claims={"company": user["company"]})

    return jsonify({"access_token": token})
