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
    """
    Authenticates a user and generates a JWT token.

    Expected JSON body:
        {
            "username": "aadil",
            "password": "1234"
        }

    Returns:
        JSON response containing access token and HTTP status code 200.
        Returns 401 if credentials are invalid.
    """
    data = request.json
    username = data["username"]
    password = data["password"]

    if username not in USERS or USERS[username]["password"] != password:
        return jsonify({"msg": "Invalid credentials"}), 401

    user = USERS[username]
    token = create_access_token(identity=username, additional_claims={"company": user["company"]})

    return jsonify({"access_token": token})
