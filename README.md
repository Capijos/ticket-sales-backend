# Ticket Sales Backend

This is the backend for a ticket sales system. This REST API allows the management of users, products, product types, shopping carts, sales, and orders. The backend is developed using SQL for the database definition.

## Table of Contents

- [Installation](#installation)
- [Database Structure](#database-structure)
- [API Endpoints](#api-endpoints)
- [Functionalities](#functionalities)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install and run the backend locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ticket-sales-backend.git
    ```

2. Navigate to the project directory:
    ```bash
    cd ticket-sales-backend
    ```

3. Set up the virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    psql -U yourusername -d yourdatabase -a -f schema.sql
    ```

5. Run the server:
    ```bash
    uvicorn main:app --reload
    ```

## Database Structure

The database is designed with the following tables:

### User
- `user_id` (SERIAL PRIMARY KEY)
- `first_name` (VARCHAR(100) NOT NULL)
- `last_name` (VARCHAR(100) NOT NULL)
- `document_id` (VARCHAR(50) UNIQUE NOT NULL)
- `age` (INTEGER NOT NULL)
- `email` (VARCHAR(254) UNIQUE NOT NULL)
- `password` (VARCHAR(255) NOT NULL)
- `created_at` (TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL)

### Product
- `product_id` (SERIAL PRIMARY KEY)
- `name` (VARCHAR(255) NOT NULL)
- `description` (TEXT)
- `images` (JSONB)
- `expiration_date` (DATE NOT NULL)
- `created_at` (TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL)

### ProductType
- `type_id` (SERIAL PRIMARY KEY)
- `product_id` (INTEGER NOT NULL REFERENCES Product(product_id) ON DELETE CASCADE)
- `type_name` (VARCHAR(100) NOT NULL)
- `price` (DECIMAL(10, 2) NOT NULL)
- `stock` (INTEGER NOT NULL)

### Cart
- `cart_id` (SERIAL PRIMARY KEY)
- `user_id` (INTEGER NOT NULL REFERENCES User(user_id) ON DELETE CASCADE)
- `created_at` (TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL)

### CartItem
- `cart_item_id` (SERIAL PRIMARY KEY)
- `cart_id` (INTEGER NOT NULL REFERENCES Cart(cart_id) ON DELETE CASCADE)
- `product_id` (INTEGER NOT NULL REFERENCES Product(product_id) ON DELETE CASCADE)
- `type_id` (INTEGER NOT NULL REFERENCES ProductType(type_id) ON DELETE CASCADE)
- `quantity` (INTEGER NOT NULL)

### Sale
- `sale_id` (SERIAL PRIMARY KEY)
- `user_id` (INTEGER NOT NULL REFERENCES User(user_id) ON DELETE CASCADE)
- `product_id` (INTEGER NOT NULL REFERENCES Product(product_id) ON DELETE CASCADE)
- `type_id` (INTEGER NOT NULL REFERENCES ProductType(type_id) ON DELETE CASCADE)
- `quantity` (INTEGER NOT NULL)
- `total_price` (DECIMAL(10, 2) NOT NULL)
- `sale_date` (TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL)

### Order
- `order_id` (SERIAL PRIMARY KEY)
- `user_id` (INTEGER NOT NULL REFERENCES User(user_id) ON DELETE CASCADE)
- `total_price` (DECIMAL(10, 2) NOT NULL)
- `order_date` (TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL)

### OrderItem
- `order_item_id` (SERIAL PRIMARY KEY)
- `order_id` (INTEGER NOT NULL REFERENCES Order(order_id) ON DELETE CASCADE)
- `product_id` (INTEGER NOT NULL REFERENCES Product(product_id) ON DELETE CASCADE)
- `type_id` (INTEGER NOT NULL REFERENCES ProductType(type_id) ON DELETE CASCADE)
- `quantity` (INTEGER NOT NULL)
- `price` (DECIMAL(10, 2) NOT NULL)

## API Endpoints

Here are some key API endpoints provided by this backend:

- `POST /users` - Create a new user
- `GET /users/{id}` - Get a user by ID
- `POST /products` - Create a new product
- `GET /products` - Get all products
- `POST /cart` - Create a new cart
- `POST /cart/{id}/items` - Add an item to a cart
- `POST /sales` - Create a new sale
- `GET /sales/{id}` - Get a sale by ID
- `POST /orders` - Create a new order
- `GET /orders/{id}` - Get an order by ID

## Functionalities

- **User Management**: Create, read, update, and delete users.
- **Product Management**: Manage products and their types, including prices and stock.
- **Cart Management**: Users can create a cart, add items, and view cart details.
- **Sales Management**: Record sales transactions, including the user and product details.
- **Order Management**: Manage orders, including order items and total prices.

## Usage

To interact with the API, you can use tools like `curl` or Postman. Here are some example requests:

### Create a new user
```bash
curl -X POST http://localhost:8000/users -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "document_id": "12345678", "age": 30, "email": "john.doe@example.com", "password": "securepassword"}'
