# Django Multi-Database REST API Project

<<<<<<< HEAD
A Django REST Framework application that implements a multi-database architecture for managing Users, Products, and Orders. Each entity is stored in a separate SQLite database, demonstrating database routing and separation of concerns.

## 📁 Project Structure
=======
A Django REST Framework application that implements a multi-database architecture for managing Users, Products, and Orders. Each entity is stored in a separate MySQL database, demonstrating database routing, transaction management, and separation of concerns.

## 📁 Complete Folder Structure
>>>>>>> 086e136 (final commit)

```
project_Assignment/
│
├── config/                          # Main project directory
<<<<<<< HEAD
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
=======
│   │
│   ├── app/                         # Django application
│   │   ├── __init__.py             # Package initialization
│   │   ├── admin.py                # Django admin configuration for all models
│   │   ├── apps.py                 # App configuration
│   │   ├── db_router.py            # Database routing logic (routes models to specific databases)
│   │   ├── models.py               # Data models (User_Model, Product_Model, Order_Model)
│   │   ├── serializers.py          # DRF serializers with validation logic
│   │   ├── views.py                # API view sets with transaction handling
│   │   ├── urls.py                 # App-level URL configuration (empty, using router)
│   │   ├── tests.py                # Unit tests
│   │   │
│   │   └── migrations/             # Database migrations
│   │       ├── __init__.py
│   │       ├── 0001_initial.py     # Initial migration (creates all models)
│   │       └── 0002_product_model_quantity.py  # Adds quantity field to Product_Model
│   │
│   ├── config/                     # Django project settings
│   │   ├── __init__.py
│   │   ├── settings.py             # Project settings & multi-database configuration
│   │   ├── urls.py                 # Root URL configuration with API router
│   │   ├── wsgi.py                 # WSGI configuration for deployment
│   │   └── asgi.py                 # ASGI configuration for async support
│   │
│   ├── manage.py                   # Django management script
│   │
│   └── __pycache__/                # Python bytecode cache (auto-generated)
│
└── README.md                       # Project documentation
>>>>>>> 086e136 (final commit)
```

## 🏗️ Architecture Overview

### Database Architecture
<<<<<<< HEAD
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
=======
The project uses **three separate MySQL databases**:

1. **`user_db`** (default) - Stores user information
2. **`products_db`** - Stores product information including inventory
3. **`orders_db`** - Stores order information

### Database Configuration
- **Engine**: MySQL (`django.db.backends.mysql`)
- **Host**: localhost
- **Port**: 3306
- **User**: root
- **Database Router**: Custom `DatabaseRouter` class automatically routes database operations

### Database Routing
The `DatabaseRouter` class (`app/db_router.py`) automatically routes database operations:
- `User_Model` → `user_db` (default database)
- `Product_Model` → `products_db`
- `Order_Model` → `orders_db`

## 📦 Data Models

### 1. User_Model
- **Database**: `user_db` (default)
>>>>>>> 086e136 (final commit)
- **Fields**:
  - `id` (Auto-generated primary key)
  - `name` (CharField, max_length=100)
  - `email` (EmailField, max_length=100)

### 2. Product_Model
<<<<<<< HEAD
- **Database**: `products.db`
=======
- **Database**: `products_db`
>>>>>>> 086e136 (final commit)
- **Fields**:
  - `id` (Auto-generated primary key)
  - `name` (CharField, max_length=100)
  - `price` (FloatField)
<<<<<<< HEAD

### 3. Order_Model
- **Database**: `orders.db`
=======
  - `quantity` (IntegerField, default=0) - Inventory stock level

### 3. Order_Model
- **Database**: `orders_db`
>>>>>>> 086e136 (final commit)
- **Fields**:
  - `id` (Auto-generated primary key)
  - `user_id` (IntegerField) - References User_Model.id
  - `product_id` (IntegerField) - References Product_Model.id
<<<<<<< HEAD
  - `quantity` (IntegerField)

## 🔌 API Endpoints

All API endpoints are prefixed with `/api/`
=======
  - `quantity` (IntegerField) - Quantity ordered

## 🔌 API Endpoints

All API endpoints are prefixed with `/api/` and use Django REST Framework's ViewSets, providing full CRUD operations.
>>>>>>> 086e136 (final commit)

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

<<<<<<< HEAD
**Response**:
=======
**Response** (200 OK):
>>>>>>> 086e136 (final commit)
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
<<<<<<< HEAD
=======
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com"
>>>>>>> 086e136 (final commit)
  }
]
```

#### GET - Retrieve Single User
```http
GET /api/users/{id}/
```

<<<<<<< HEAD
**Response**:
=======
**Response** (200 OK):
>>>>>>> 086e136 (final commit)
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

<<<<<<< HEAD
=======
**Error Response** (400 Bad Request):
```json
{
  "email": ["Invalid email"]
}
```

>>>>>>> 086e136 (final commit)
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

<<<<<<< HEAD
**Response**:
=======
**Response** (200 OK):
>>>>>>> 086e136 (final commit)
```json
[
  {
    "id": 1,
    "name": "Laptop",
<<<<<<< HEAD
    "price": 999.99
=======
    "price": 999.99,
    "quantity": 50
  },
  {
    "id": 2,
    "name": "Smartphone",
    "price": 599.99,
    "quantity": 100
>>>>>>> 086e136 (final commit)
  }
]
```

#### GET - Retrieve Single Product
```http
GET /api/products/{id}/
```

<<<<<<< HEAD
**Response**:
=======
**Response** (200 OK):
>>>>>>> 086e136 (final commit)
```json
{
  "id": 1,
  "name": "Laptop",
<<<<<<< HEAD
  "price": 999.99
=======
  "price": 999.99,
  "quantity": 50
>>>>>>> 086e136 (final commit)
}
```

#### POST - Create Product
```http
POST /api/products/
Content-Type: application/json

{
  "name": "Smartphone",
<<<<<<< HEAD
  "price": 599.99
=======
  "price": 599.99,
  "quantity": 100
>>>>>>> 086e136 (final commit)
}
```

**Response** (201 Created):
```json
{
  "id": 2,
  "name": "Smartphone",
<<<<<<< HEAD
  "price": 599.99
=======
  "price": 599.99,
  "quantity": 100
>>>>>>> 086e136 (final commit)
}
```

**Validation Rules**:
- `price` must be >= 0 (cannot be negative)
- `name` is required (max 100 characters)
<<<<<<< HEAD
=======
- `quantity` defaults to 0 if not provided

**Error Response** (400 Bad Request):
```json
{
  "price": ["Price cannot be negative"]
}
```
>>>>>>> 086e136 (final commit)

#### PUT - Update Product (Full Update)
```http
PUT /api/products/{id}/
Content-Type: application/json

{
  "name": "Gaming Laptop",
<<<<<<< HEAD
  "price": 1299.99
=======
  "price": 1299.99,
  "quantity": 25
>>>>>>> 086e136 (final commit)
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

<<<<<<< HEAD
**Response**:
=======
**Response** (200 OK):
>>>>>>> 086e136 (final commit)
```json
[
  {
    "id": 1,
    "user_id": 1,
    "product_id": 1,
    "quantity": 2
<<<<<<< HEAD
=======
  },
  {
    "id": 2,
    "user_id": 2,
    "product_id": 2,
    "quantity": 1
>>>>>>> 086e136 (final commit)
  }
]
```

#### GET - Retrieve Single Order
```http
GET /api/orders/{id}/
```

<<<<<<< HEAD
**Response**:
=======
**Response** (200 OK):
>>>>>>> 086e136 (final commit)
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
<<<<<<< HEAD
- `user_id` must exist in `users.db`
- `product_id` must exist in `products.db`
- `quantity` must be > 0

**Error Responses**:
- If user doesn't exist:
=======
- `user_id` must exist in `user_db`
- `product_id` must exist in `products_db`
- `quantity` must be > 0
- Product must have sufficient stock (`product.quantity >= order.quantity`)

**Error Responses**:

- If user doesn't exist (400 Bad Request):
>>>>>>> 086e136 (final commit)
```json
{
  "user_id": ["User does not exist in users database"]
}
```

<<<<<<< HEAD
- If product doesn't exist:
=======
- If product doesn't exist (400 Bad Request):
>>>>>>> 086e136 (final commit)
```json
{
  "product_id": ["Product does not exist in products database"]
}
```

<<<<<<< HEAD
- If quantity is invalid:
=======
- If quantity is invalid (400 Bad Request):
>>>>>>> 086e136 (final commit)
```json
{
  "quantity": ["Quantity must be greater than 0"]
}
```

<<<<<<< HEAD
=======
- If product is out of stock (400 Bad Request):
```json
{
  "non_field_errors": ["Product out of stock"]
}
```

>>>>>>> 086e136 (final commit)
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

<<<<<<< HEAD
=======
## 🛒 Orders Feature Explanation

The **Orders Feature** is a comprehensive order management system that handles the creation and management of orders across multiple databases with proper validation and inventory management.

### Key Components:

1. **Order Model** (`Order_Model`):
   - Stores order information in the `orders_db` database
   - Contains references to users (`user_id`) and products (`product_id`)
   - Tracks the quantity of items ordered

2. **Order Serializer** (`OrderSerializer`):
   - Validates order data before creation
   - Ensures `user_id` exists in the users database
   - Ensures `product_id` exists in the products database
   - Validates that quantity is greater than 0

3. **Order ViewSet** (`OrderViewSet`):
   - Provides CRUD operations for orders
   - Implements transaction management for order creation
   - Handles inventory stock checking and deduction

### Order Creation Flow:

1. **Validation Phase** (Serializer):
   - Validates user exists in `user_db`
   - Validates product exists in `products_db`
   - Validates quantity > 0

2. **Transaction Phase** (ViewSet):
   - Starts a database transaction on `products_db`
   - Locks the product record using `select_for_update()` to prevent race conditions
   - Checks if product has sufficient stock
   - Deducts the ordered quantity from product inventory
   - Saves the updated product

3. **Order Creation Phase**:
   - Creates the order record in `orders_db`
   - Returns the created order

### Features:

- **Cross-Database Validation**: Validates references across different databases
- **Inventory Management**: Automatically deducts stock when orders are created
- **Stock Checking**: Prevents orders when products are out of stock
- **Data Integrity**: Ensures all referenced entities exist before order creation

---

## 🔄 Transaction Feature Explanation

The **Transaction Feature** ensures data consistency and prevents race conditions when creating orders, especially when multiple users try to order the same product simultaneously.

### Implementation Details:

The transaction feature is implemented in the `OrderViewSet.perform_create()` method using Django's `transaction.atomic()` context manager.

### Key Components:

1. **Atomic Transaction**:
   ```python
   with transaction.atomic(using='products_db'):
   ```
   - Ensures all database operations within the block either complete successfully or are rolled back
   - Uses `products_db` database specifically

2. **Row-Level Locking**:
   ```python
   product = Product_Model.objects.using('products_db') \
       .select_for_update() \
       .get(id=product_id)
   ```
   - `select_for_update()` locks the product row until the transaction completes
   - Prevents concurrent modifications to the same product
   - Ensures accurate stock checking and deduction

3. **Stock Validation**:
   ```python
   if product.quantity < quantity:
       raise ValidationError("Product out of stock")
   ```
   - Checks if sufficient stock is available
   - Raises an error if stock is insufficient

4. **Inventory Deduction**:
   ```python
   product.quantity -= quantity
   product.save(using='products_db')
   ```
   - Deducts the ordered quantity from product inventory
   - Saves the updated product within the transaction

### How It Works:

1. **Transaction Start**: When an order is created, a transaction begins on `products_db`
2. **Lock Acquisition**: The product row is locked using `select_for_update()`
3. **Stock Check**: The system checks if sufficient stock is available
4. **Stock Deduction**: If stock is available, the quantity is deducted
5. **Transaction Commit**: The transaction commits, releasing the lock
6. **Order Creation**: The order is created in `orders_db`

### Benefits:

- **Data Consistency**: Ensures inventory is accurately maintained
- **Race Condition Prevention**: Prevents multiple orders from overselling products
- **Atomic Operations**: All-or-nothing approach - if any step fails, everything rolls back
- **Concurrency Safety**: Handles simultaneous order requests correctly

### Example Scenario:

**Without Transactions** (Problem):
- User A checks stock: 10 items available
- User B checks stock: 10 items available (before User A completes)
- User A orders 8 items → Stock becomes 2
- User B orders 8 items → Stock becomes -6 (overselling!)

**With Transactions** (Solution):
- User A locks product → checks stock: 10 items → orders 8 → releases lock → Stock: 2
- User B waits for lock → locks product → checks stock: 2 items → order fails (insufficient stock)

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- MySQL Server installed and running
- MySQL databases created: `user_db`, `products_db`, `orders_db`

### Step 1: Create Virtual Environment
```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies
```bash
pip install django djangorestframework mysqlclient
```

Or create `requirements.txt`:
```txt
Django==6.0
djangorestframework
mysqlclient
```

Then install:
```bash
pip install -r requirements.txt
```

### Step 4: Configure MySQL Databases
Create three MySQL databases:
```sql
CREATE DATABASE user_db;
CREATE DATABASE products_db;
CREATE DATABASE orders_db;
```

### Step 5: Update Database Credentials
Edit `config/config/settings.py` and update database credentials if needed:
- `USER`: Your MySQL username
- `PASSWORD`: Your MySQL password
- `HOST`: MySQL host (default: localhost)
- `PORT`: MySQL port (default: 3306)

### Step 6: Navigate to Project Directory
```bash
cd config
```

### Step 7: Run Database Migrations
Since the project uses multiple databases, run migrations for each database:

```bash
# Migrate default database (user_db)
python manage.py migrate

# Migrate products database
python manage.py migrate --database=products_db

# Migrate orders database
python manage.py migrate --database=orders_db
```

### Step 8: Create Superuser (Optional)
To access Django admin panel:
```bash
python manage.py createsuperuser
```

### Step 9: Run Development Server
```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

---

>>>>>>> 086e136 (final commit)
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
<<<<<<< HEAD
  -d '{"name": "Laptop", "price": 999.99}'
=======
  -d '{"name": "Laptop", "price": 999.99, "quantity": 50}'
>>>>>>> 086e136 (final commit)
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
<<<<<<< HEAD
product_data = {"name": "Laptop", "price": 999.99}
=======
product_data = {"name": "Laptop", "price": 999.99, "quantity": 50}
>>>>>>> 086e136 (final commit)
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

<<<<<<< HEAD
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
=======
---
>>>>>>> 086e136 (final commit)

## 🛠️ Django Admin Interface

Access the admin panel at: `http://127.0.0.1:8000/admin/`

All three models are registered in the admin:
<<<<<<< HEAD
- **User_Model** - Uses default database
- **Product_Model** - Uses `products_db` (custom queryset/save methods)
- **Order_Model** - Uses `orders_db` (custom queryset/save methods)

=======
- **User_Model** - Uses default database (`user_db`)
- **Product_Model** - Uses `products_db` (custom queryset/save methods)
- **Order_Model** - Uses `orders_db` (custom queryset/save methods)

The admin interface properly handles multi-database operations with custom queryset and save methods.

---

>>>>>>> 086e136 (final commit)
## 📝 Validation Rules Summary

### User Serializer
- ✅ Email must contain "@" symbol
- ✅ Name and email are required fields
<<<<<<< HEAD

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
=======
- ✅ Max length: 100 characters for both fields

### Product Serializer
- ✅ Price must be >= 0 (non-negative)
- ✅ Name is required (max 100 characters)
- ✅ Quantity defaults to 0 if not provided

### Order Serializer
- ✅ `user_id` must reference an existing user in `user_db`
- ✅ `product_id` must reference an existing product in `products_db`
- ✅ Quantity must be > 0
- ✅ Product must have sufficient stock (checked in transaction)

---

## 🔍 Key Features

1. **Multi-Database Architecture**: Separate MySQL databases for different entities
2. **Database Routing**: Automatic routing of queries to appropriate databases via custom router
3. **RESTful API**: Full CRUD operations via Django REST Framework ViewSets
4. **Data Validation**: Comprehensive validation at serializer level
5. **Transaction Management**: Atomic transactions with row-level locking for order creation
6. **Inventory Management**: Automatic stock deduction when orders are created
7. **Race Condition Prevention**: `select_for_update()` prevents concurrent order issues
8. **Admin Interface**: Django admin configured for all models with proper database routing
9. **Cross-Database Validation**: Validates references across different databases

---
>>>>>>> 086e136 (final commit)

## 🐛 Troubleshooting

### Issue: Migration errors
**Solution**: Make sure to run migrations for all three databases:
```bash
python manage.py migrate
python manage.py migrate --database=products_db
python manage.py migrate --database=orders_db
```

<<<<<<< HEAD
### Issue: Database not found
**Solution**: The databases are created automatically when you run migrations. If they don't exist, run the migration commands above.

### Issue: Order creation fails with "User does not exist"
**Solution**: Ensure the `user_id` you're using exists in the `users.db`. Create a user first before creating an order.

### Issue: Order creation fails with "Product does not exist"
**Solution**: Ensure the `product_id` you're using exists in the `products.db`. Create a product first before creating an order.
=======
### Issue: MySQL connection error
**Solution**: 
- Ensure MySQL server is running
- Verify database credentials in `settings.py`
- Ensure databases exist: `user_db`, `products_db`, `orders_db`
- Check MySQL user has proper permissions

### Issue: Order creation fails with "User does not exist"
**Solution**: Ensure the `user_id` you're using exists in the `user_db`. Create a user first before creating an order.

### Issue: Order creation fails with "Product does not exist"
**Solution**: Ensure the `product_id` you're using exists in the `products_db`. Create a product first before creating an order.

### Issue: Order creation fails with "Product out of stock"
**Solution**: The product doesn't have sufficient quantity. Check product inventory or reduce order quantity.

### Issue: Import errors for mysqlclient
**Solution**: Install MySQL development libraries:
- **Windows**: Download MySQL Connector/C or use `pip install mysqlclient` (requires Visual C++ Build Tools)
- **Linux**: `sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`
- **Mac**: `brew install mysql pkg-config`

---
>>>>>>> 086e136 (final commit)

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Django Database Routing](https://docs.djangoproject.com/en/stable/topics/db/multi-db/)
<<<<<<< HEAD
=======
- [Django Transactions](https://docs.djangoproject.com/en/stable/topics/db/transactions/)

---
>>>>>>> 086e136 (final commit)

## 📄 License

This project is for educational/assignment purposes.

<<<<<<< HEAD
## 👤 Author

Project Assignment - Multi-Database Django REST API

---

**Note**: This project demonstrates advanced Django concepts including multi-database setup, database routing, and RESTful API design with proper validation.
=======
---

## 👤 Author

Project Assignment - Multi-Database Django REST API with Transaction Management

---

**Note**: This project demonstrates advanced Django concepts including multi-database setup, database routing, RESTful API design with proper validation, transaction management, and concurrent order handling with inventory management.
>>>>>>> 086e136 (final commit)

