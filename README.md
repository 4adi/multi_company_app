# Multi-Company Product Management API (Flask + MongoDB)

A complete multi-tenant REST API with:

- Separate DB for each company
- JWT authentication
- Authorization middleware
- Product creation API
- Migration script

---

## 🚀 How It Works

### 1. Login
Send:
```json
{
  "username": "aadil",
  "password": "1234"
}

Response:
{
  "access_token": "<JWT>"
}


2. Add Product

Add header:
Authorization: Bearer <JWT>

Body:
{
  "name": "Laptop",
  "description": "Super fast",
  "image_url": "http://image.com/laptop.png"
}


🛠 Setup

Install dependencies
pip install -r requirements.txt

Create MongoDB databases
python migrations/create_company_dbs.py

Run backend
python app.py

Backend runs at:
http://localhost:5000
