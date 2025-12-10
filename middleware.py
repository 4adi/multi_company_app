# This middleware extracts company info from JWT and attaches the DB connection to the request.

from flask import g
from flask_jwt_extended import get_jwt
from db_manager import get_company_db

def inject_company_db():
    """
    Extract company name from JWT and attach DB instance to request context.
    """
    claims = get_jwt()
    company = claims["company"]
    g.db = get_company_db(company)
