
# For running the migration script file
# run the command - python migrations/create_company_dbs.py



from pymongo import MongoClient
from config import MONGO_BASE_URL, COMPANY_DATABASES

client = MongoClient(MONGO_BASE_URL)

for company, db_name in COMPANY_DATABASES.items():
    db = client[db_name]
    db.create_collection("products")
    print(f"Created DB + collection for {company}")
