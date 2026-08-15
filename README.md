# Inventory Management System

A Django REST Framework API for managing inventory, customers, and invoices, built with a custom user model, role-based permissions, and invoice reporting.

## Features

- **Custom User Model** — extends `AbstractUser` with a `role` field (`ADMIN`, `STAFF`, `VIEWER`) and a custom manager (`create_user` / `create_superuser`).
- **User Profile Management** — each user has a `Profile` (phone number, address, bio), automatically created via a signal when the user is created. Users can view and update their own profile via `/api/profiles/me/`.
- **Category & Product Management** — full CRUD on `Category` and `Product`, with `Product` validation on price and stock quantity.
- **Customer & Invoice Management** — `Customer` model, and multi-line `Invoice`/`InvoiceItem` support (one invoice can contain multiple products). Each `InvoiceItem` snapshots the price at time of sale.
- **Permission Classes** — only `ADMIN`/`STAFF` users can create, update, or delete Products and Invoices. All authenticated users can read.
- **Invoice Report/Summary** — a read-only endpoint returning total invoices, total sales, and total products sold.

## Tech Stack

- Django
- Django REST Framework
- djangorestframework-simplejwt (JWT authentication)

## Setup

1. Clone the repository and navigate into it.
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```
3. Install dependencies:
   ```
   python -m pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
6. Start the server:
   ```
   python manage.py runserver
   ```

## Authentication

This API uses JWT authentication.

- `POST /api/token/` — obtain an access/refresh token pair (body: `username`, `password`)
- `POST /api/token/refresh/` — refresh an access token

Include the access token on all other requests as a header:
```
Authorization: Bearer <access_token>
```

## API Endpoints

### Profile
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/profiles/me/` | View your own profile |
| PATCH | `/api/profiles/me/` | Update your own profile |

### Category
| Method | Endpoint | Description |
|---|---|---|
| GET / POST | `/api/inventory/categories/` | List / create categories |
| GET / PUT / PATCH / DELETE | `/api/inventory/categories/{id}/` | Retrieve / update / delete a category |

### Product
| Method | Endpoint | Description | Access |
|---|---|---|---|
| GET | `/api/inventory/products/` | List / retrieve products | Any authenticated user |
| POST / PUT / PATCH / DELETE | `/api/inventory/products/` | Create / update / delete products | ADMIN / STAFF only |

### Customer
| Method | Endpoint | Description |
|---|---|---|
| GET / POST | `/api/inventory/customers/` | List / create customers |
| GET / PUT / PATCH / DELETE | `/api/inventory/customers/{id}/` | Retrieve / update / delete a customer |

### Invoice
| Method | Endpoint | Description | Access |
|---|---|---|---|
| GET | `/api/invoices/invoices/` | List / retrieve invoices | Any authenticated user |
| POST / PUT / PATCH / DELETE | `/api/invoices/invoices/` | Create / update / delete invoices | ADMIN / STAFF only |

Example invoice creation body (supports multiple line items):
```json
{
    "customer": 1,
    "items": [
        { "product": 1, "quantity": 2, "price": "19.99" },
        { "product": 2, "quantity": 1, "price": "9.99" }
    ]
}
```

### Report
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/invoices/reports/invoice/` | Total invoices, total sales, total products sold |

## Roles

- **ADMIN** — full access, including modifying products and invoices.
- **STAFF** — can create/edit products and invoices.
- **VIEWER** (default) — read-only access.