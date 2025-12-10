# This middleware extracts company info from JWT and attaches the DB connection to the request.

from flask import g
from flask_jwt_extended import get_jwt
from db_manager import get_company_db

def inject_company_db():
    """
    Middleware responsible for injecting the correct MongoDB instance
    into the Flask 'g' context based on the company encoded in the JWT.

    - Verifies JWT validity
    - Extracts company name from the token
    - Fetches company-specific DB
    - Makes DB available for the request lifecycle

    Raises:
        Exception: If token is invalid or company is missing.
    """
    claims = get_jwt()
    company = claims["company"]
    g.db = get_company_db(company)
