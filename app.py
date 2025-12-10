from flask import Flask
from flask_jwt_extended import JWTManager
from auth_routes import auth_bp
from product_routes import product_bp
from middleware import inject_company_db

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "mysecretkey"

jwt = JWTManager(app)

@app.before_request
def before_request():
    """
    Middleware hook executed before every request.

    This function tries to inject the correct company database
    based on the JWT token provided in the request.

    If a public route (like login) is hit, it safely ignores failures.
    """
    try:
        inject_company_db()
    except Exception:
        pass

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(product_bp, url_prefix="/products")

if __name__ == "__main__":
    """
    Entry point of the application.
    
    Runs the Flask development server.
    """
    app.run(debug=True)
