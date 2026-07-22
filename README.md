# Event Management API

A RESTful API built with **FastAPI** for managing personal events. The application provides secure user authentication using JWT (JSON Web Tokens) and allows authenticated users to create, organize, search, filter, sort, update, and delete their own events.

---

## Features

### User Management

- User registration
- Secure login with JWT authentication
- Password hashing using bcrypt
- Retrieve authenticated user information

### Event Management

- Create events
- View all personal events
- Retrieve a specific event
- Update existing events
- Delete events
- Filter events by date and/or location
- Search events by keyword (title or description)
- Sort events by:
  - Date
  - Title
  - Location
- Ascending and descending sorting
- Users can only manage their own events

---

## Technologies Used

- Python 3
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- JWT Authentication (python-jose)
- Passlib (bcrypt)
- Uvicorn

---

## Project Structure

```
.
├── main.py
├── database.py
├── security.py
│
├── models/
│   ├── user.py
│   └── event.py
│
├── schemas/
│   ├── user.py
│   └── event.py
│
└── routers/
    ├── users.py
    └── events.py
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd <repository-name>
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose passlib[bcrypt] python-multipart email-validator
```

### Configure PostgreSQL

Update the database connection string inside `database.py`:

```python
DATABASE_URL = "postgresql://username:password@localhost:5432/database_name"
```

Create the PostgreSQL database before starting the application.

### Run the application

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8050
```

Swagger UI:

```
http://127.0.0.1:8050/docs
```

ReDoc:

```
http://127.0.0.1:8050/redoc
```

---

## Authentication

The API uses **JWT Bearer Authentication**.

Workflow:

1. Register a user.
2. Login using email and password.
3. Receive a JWT access token.
4. Click **Authorize** in Swagger UI.
5. Enter:

```
Bearer <your_access_token>
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Authenticate user |
| GET | `/me` | Retrieve authenticated user |

---

### Events

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/events` | Create a new event |
| GET | `/events` | Retrieve all events |
| GET | `/events/{id}` | Retrieve an event by ID |
| PUT | `/events/{id}` | Update an event |
| DELETE | `/events/{id}` | Delete an event |
| GET | `/events/filter` | Filter events by date and/or location |
| GET | `/events/search` | Search events by keyword |
| GET | `/events/sort` | Sort events by date, title, or location |

---

## Event Model

```json
{
  "title": "Project Meeting",
  "description": "Weekly team meeting",
  "date": "2026-07-20",
  "time": "10:00",
  "location": "Office"
}
```

---

## Security

- Passwords are securely hashed using bcrypt.
- JWT access tokens protect private endpoints.
- Users can only access their own events.
- Authentication is required for every event-related endpoint.

---

## Database

The project uses **PostgreSQL** together with **SQLAlchemy ORM**.

Current entities:

### User

- id
- username
- email
- hashed_password

### Event

- id
- title
- description
- date
- time
- location
- user_id

Each event belongs to exactly one user through a foreign key relationship.

---

## Interactive API Documentation

FastAPI automatically generates API documentation.

- Swagger UI: `/docs`
- ReDoc: `/redoc`

Each endpoint includes:
- Summary
- Description
- Request models
- Response models
- Authentication requirements

---

## License

This project was developed for educational purposes.
