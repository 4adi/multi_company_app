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
    try:
        inject_company_db()
    except Exception:
        pass

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(product_bp, url_prefix="/products")

if __name__ == "__main__":
    app.run(debug=True)
