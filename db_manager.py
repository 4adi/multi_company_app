# Select the correct company DB based on the user.


from pymongo import MongoClient
from config import MONGO_BASE_URL, COMPANY_DATABASES

client = MongoClient(MONGO_BASE_URL)

def get_company_db(company_name):
    """
    Returns a MongoDB database instance for the given company.

    Args:
        company_name (str): The company identifier extracted from JWT.

    Raises:
        Exception: If the company name is not listed in COMPANY_DATABASES.

    Returns:
        Database: A PyMongo database instance for the specific company.
    """
    if company_name not in COMPANY_DATABASES:
        raise Exception("Invalid company name")
    
    db_name = COMPANY_DATABASES.get(company_name)
    return client[db_name]
