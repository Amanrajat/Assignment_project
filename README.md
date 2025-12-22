# Django Multi-Database REST API Project

A Django REST Framework application that implements a multi-database architecture for managing Users, Products, and Orders. Each entity is stored in a separate SQLite database, demonstrating database routing and separation of concerns.

## 📁 Project Structure

```
project_Assignment/
│
├── config/                          # Main project directory
│   ├── app/                         # Django application
│   │   ├── __init__.py
│   │   ├── admin.py                 # Django admin configuration
│   │   ├── apps.py                  # App configuration
│   │   ├── db_router.py             # Database routing logic
│   │   ├── models.py                # Data models (User, Product, Order)
│   │   ├── serializers.py           # DRF serializers with validation
│   │   ├── views.py                 # API view sets
│   │   ├── urls.py                  # App-level URL configuration (empty)
│   │   ├── tests.py                 # Unit tests
│   │   └── migrations/              # Database migrations
│   │       ├── __init__.py
│   │       └── 0001_initial.py      # Initial migration
│   │
│   ├── config/                      # Django project settings
│   │   ├── __init__.py
│   │   ├── settings.py              # Project settings & database config
│   │   ├── urls.py                  # Root URL configuration
│   │   ├── wsgi.py                  # WSGI configuration
│   │   └── asgi.py                  # ASGI configuration
│   │
│   ├── manage.py                    # Django management script
│   ├── users.db                     # SQLite database for users
│   ├── products.db                  # SQLite database for products
│   └── orders.db                    # SQLite database for orders
│
└── README.md                        # This file
```

## 🏗️ Architecture Overview

### Database Architecture
The project uses **three separate SQLite databases**:

1. **`users.db`** (default) - Stores user information
2. **`products.db`** - Stores product information
3. **`orders.db`** - Stores order information

### Database Routing
A custom `DatabaseRouter` class (`app/db_router.py`) automatically routes database operations:
- `User_Model` → `users.db` (default)
- `Product_Model` → `products.db`
- `Order_Model` → `orders.db`

## 📦 Dependencies

### Required Packages
- **Django** (6.0)
- **Django REST Framework** (djangorestframework)

### Installation

1. **Create a virtual environment** (recommended):
```bash
python -m venv venv
```

2. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**:
```bash
pip install django djangorestframework
```

4. **Create requirements.txt** (optional):
```bash
pip freeze > requirements.txt
```

## 🚀 Setup Instructions

### Step 1: Navigate to Project Directory
```bash
cd config
```

### Step 2: Run Database Migrations

Since the project uses multiple databases, you need to run migrations for each database:

```bash
# Migrate default database (users.db)
python manage.py migrate

# Migrate products database
python manage.py migrate --database=products_db

# Migrate orders database
python manage.py migrate --database=orders_db
```

### Step 3: Create Superuser (Optional)
To access Django admin panel:
```bash
python manage.py createsuperuser
```

### Step 4: Run Development Server
```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

## 📊 Data Models

### 1. User_Model
- **Database**: `users.db` (default)
- **Fields**:
  - `id` (Auto-generated primary key)
  - `name` (CharField, max_length=100)
  - `email` (EmailField, max_length=100)

### 2. Product_Model
- **Database**: `products.db`
- **Fields**:
  - `id` (Auto-generated primary key)
  - `name` (CharField, max_length=100)
  - `price` (FloatField)

### 3. Order_Model
- **Database**: `orders.db`
- **Fields**:
  - `id` (Auto-generated primary key)
  - `user_id` (IntegerField) - References User_Model.id
  - `product_id` (IntegerField) - References Product_Model.id
  - `quantity` (IntegerField)

## 🔌 API Endpoints

All API endpoints are prefixed with `/api/`

### Base URL
```
http://127.0.0.1:8000/api/
```

---

### 1. Users API

**Base Endpoint**: `/api/users/`

#### GET - List All Users
```http
GET /api/users/
```

**Response**:
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
]
```

#### GET - Retrieve Single User
```http
GET /api/users/{id}/
```

**Response**:
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

#### POST - Create User
```http
POST /api/users/
Content-Type: application/json

{
  "name": "Jane Smith",
  "email": "jane@example.com"
}
```

**Response** (201 Created):
```json
{
  "id": 2,
  "name": "Jane Smith",
  "email": "jane@example.com"
}
```

**Validation Rules**:
- `email` must contain "@" symbol
- `name` is required (max 100 characters)
- `email` is required (max 100 characters)

#### PUT - Update User (Full Update)
```http
PUT /api/users/{id}/
Content-Type: application/json

{
  "name": "Jane Doe",
  "email": "jane.doe@example.com"
}
```

#### PATCH - Partial Update User
```http
PATCH /api/users/{id}/
Content-Type: application/json

{
  "email": "newemail@example.com"
}
```

#### DELETE - Delete User
```http
DELETE /api/users/{id}/
```

**Response**: 204 No Content

---

### 2. Products API

**Base Endpoint**: `/api/products/`

#### GET - List All Products
```http
GET /api/products/
```

**Response**:
```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 999.99
  }
]
```

#### GET - Retrieve Single Product
```http
GET /api/products/{id}/
```

**Response**:
```json
{
  "id": 1,
  "name": "Laptop",
  "price": 999.99
}
```

#### POST - Create Product
```http
POST /api/products/
Content-Type: application/json

{
  "name": "Smartphone",
  "price": 599.99
}
```

**Response** (201 Created):
```json
{
  "id": 2,
  "name": "Smartphone",
  "price": 599.99
}
```

**Validation Rules**:
- `price` must be >= 0 (cannot be negative)
- `name` is required (max 100 characters)

#### PUT - Update Product (Full Update)
```http
PUT /api/products/{id}/
Content-Type: application/json

{
  "name": "Gaming Laptop",
  "price": 1299.99
}
```

#### PATCH - Partial Update Product
```http
PATCH /api/products/{id}/
Content-Type: application/json

{
  "price": 899.99
}
```

#### DELETE - Delete Product
```http
DELETE /api/products/{id}/
```

**Response**: 204 No Content

---

### 3. Orders API

**Base Endpoint**: `/api/orders/`

#### GET - List All Orders
```http
GET /api/orders/
```

**Response**:
```json
[
  {
    "id": 1,
    "user_id": 1,
    "product_id": 1,
    "quantity": 2
  }
]
```

#### GET - Retrieve Single Order
```http
GET /api/orders/{id}/
```

**Response**:
```json
{
  "id": 1,
  "user_id": 1,
  "product_id": 1,
  "quantity": 2
}
```

#### POST - Create Order
```http
POST /api/orders/
Content-Type: application/json

{
  "user_id": 1,
  "product_id": 1,
  "quantity": 3
}
```

**Response** (201 Created):
```json
{
  "id": 1,
  "user_id": 1,
  "product_id": 1,
  "quantity": 3
}
```

**Validation Rules**:
- `user_id` must exist in `users.db`
- `product_id` must exist in `products.db`
- `quantity` must be > 0

**Error Responses**:
- If user doesn't exist:
```json
{
  "user_id": ["User does not exist in users database"]
}
```

- If product doesn't exist:
```json
{
  "product_id": ["Product does not exist in products database"]
}
```

- If quantity is invalid:
```json
{
  "quantity": ["Quantity must be greater than 0"]
}
```

#### PUT - Update Order (Full Update)
```http
PUT /api/orders/{id}/
Content-Type: application/json

{
  "user_id": 2,
  "product_id": 2,
  "quantity": 5
}
```

#### PATCH - Partial Update Order
```http
PATCH /api/orders/{id}/
Content-Type: application/json

{
  "quantity": 4
}
```

#### DELETE - Delete Order
```http
DELETE /api/orders/{id}/
```

**Response**: 204 No Content

---

## 🧪 Testing the API

### Using cURL

#### Create a User
```bash
curl -X POST http://127.0.0.1:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

#### Create a Product
```bash
curl -X POST http://127.0.0.1:8000/api/products/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Laptop", "price": 999.99}'
```

#### Create an Order
```bash
curl -X POST http://127.0.0.1:8000/api/orders/ \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "product_id": 1, "quantity": 2}'
```

#### Get All Users
```bash
curl http://127.0.0.1:8000/api/users/
```

### Using Python Requests

```python
import requests

BASE_URL = "http://127.0.0.1:8000/api"

# Create a user
user_data = {"name": "John Doe", "email": "john@example.com"}
response = requests.post(f"{BASE_URL}/users/", json=user_data)
print(response.json())

# Create a product
product_data = {"name": "Laptop", "price": 999.99}
response = requests.post(f"{BASE_URL}/products/", json=product_data)
print(response.json())

# Create an order
order_data = {"user_id": 1, "product_id": 1, "quantity": 2}
response = requests.post(f"{BASE_URL}/orders/", json=order_data)
print(response.json())
```

### Using Postman or Insomnia

1. Set method to `GET`, `POST`, `PUT`, `PATCH`, or `DELETE`
2. Enter URL: `http://127.0.0.1:8000/api/{endpoint}/`
3. For POST/PUT/PATCH, set `Content-Type: application/json` in headers
4. Add JSON body for POST/PUT/PATCH requests

## 🔧 Configuration Details

### Database Configuration (`config/settings.py`)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'users.db',
    },
    'products_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'products.db',
    },
    'orders_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'orders.db',
    },
}

DATABASE_ROUTERS = ['app.db_router.DatabaseRouter']
```

### Installed Apps

- `django.contrib.admin` - Django admin interface
- `django.contrib.auth` - Authentication system
- `django.contrib.contenttypes` - Content types framework
- `django.contrib.sessions` - Session framework
- `django.contrib.messages` - Messaging framework
- `django.contrib.staticfiles` - Static files handling
- `rest_framework` - Django REST Framework
- `app` - Custom application

## 🛠️ Django Admin Interface

Access the admin panel at: `http://127.0.0.1:8000/admin/`

All three models are registered in the admin:
- **User_Model** - Uses default database
- **Product_Model** - Uses `products_db` (custom queryset/save methods)
- **Order_Model** - Uses `orders_db` (custom queryset/save methods)

## 📝 Validation Rules Summary

### User Serializer
- ✅ Email must contain "@" symbol
- ✅ Name and email are required fields

### Product Serializer
- ✅ Price must be >= 0 (non-negative)
- ✅ Name is required

### Order Serializer
- ✅ `user_id` must reference an existing user in `users.db`
- ✅ `product_id` must reference an existing product in `products.db`
- ✅ Quantity must be > 0

## 🔍 Key Features

1. **Multi-Database Architecture**: Separate databases for different entities
2. **Database Routing**: Automatic routing of queries to appropriate databases
3. **RESTful API**: Full CRUD operations via Django REST Framework
4. **Data Validation**: Comprehensive validation at serializer level
5. **Admin Interface**: Django admin configured for all models with proper database routing

## 🐛 Troubleshooting

### Issue: Migration errors
**Solution**: Make sure to run migrations for all three databases:
```bash
python manage.py migrate
python manage.py migrate --database=products_db
python manage.py migrate --database=orders_db
```

### Issue: Database not found
**Solution**: The databases are created automatically when you run migrations. If they don't exist, run the migration commands above.

### Issue: Order creation fails with "User does not exist"
**Solution**: Ensure the `user_id` you're using exists in the `users.db`. Create a user first before creating an order.

### Issue: Order creation fails with "Product does not exist"
**Solution**: Ensure the `product_id` you're using exists in the `products.db`. Create a product first before creating an order.

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Django Database Routing](https://docs.djangoproject.com/en/stable/topics/db/multi-db/)

## 📄 License

This project is for educational/assignment purposes.

## 👤 Author

Project Assignment - Multi-Database Django REST API

---

**Note**: This project demonstrates advanced Django concepts including multi-database setup, database routing, and RESTful API design with proper validation.

