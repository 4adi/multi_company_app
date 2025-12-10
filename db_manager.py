# Select the correct company DB based on the user.


from pymongo import MongoClient
from config import MONGO_BASE_URL, COMPANY_DATABASES

client = MongoClient(MONGO_BASE_URL)

def get_company_db(company_name):
    if company_name not in COMPANY_DATABASES:
        raise Exception("Invalid company name")
    
    db_name = COMPANY_DATABASES.get(company_name)
    return client[db_name]
