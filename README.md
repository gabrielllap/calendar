Event Management API

A RESTful API built with FastAPI for managing personal events. The
application provides secure user authentication using JWT tokens and
allows authenticated users to create, manage, update, and delete their
own events.

Features

-   User registration
-   User authentication with JWT
-   Password hashing using bcrypt
-   Protected API endpoints
-   Create new events
-   View all personal events
-   View a specific event
-   Update existing events
-   Delete events
-   Filter events by date or location
-   User authorization (users can only access their own events)

Technologies Used

-   Python
-   FastAPI
-   SQLAlchemy
-   PostgreSQL
-   Pydantic
-   JWT Authentication (python-jose)
-   Passlib (bcrypt)

Project Structure

. ├── main.py
├── database.py 
├── security.py
├── models/
  │ ├── user.py
  │ └── event.py 
├── routers/
  │ ├── users.py 
  │ └── events.py 
└── schemas/
  ├── user.py
  └── event.py

Installation

1.  Clone the repository.
2.  Create a virtual environment.
3.  Install dependencies:

pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose
passlib[bcrypt] python-multipart email-validator

4.  Configure the DATABASE_URL in database.py.
5.  Start the server:

uvicorn main:app –reload

API: http://127.0.0.1:8050

Swagger Docs: http://127.0.0.1:8050/docs

Authentication

Register a new account, log in to receive a JWT token, then authorize
using:

Bearer

API Endpoints

Authentication - POST /register - POST /login - GET /me

Events - POST /events - GET /events - GET /events/{id} - PUT
/events/{id} - DELETE /events/{id} - GET /events/filter

Event Model

{ “title”: “Project Meeting”, “description”: “Weekly team meeting”,
“date”: “2026-07-20”, “time”: “10:00”, “location”: “Office” }

Security

-   Passwords are hashed using bcrypt.
-   JWT protects private endpoints.
-   Users can only access and modify their own events.

Database

Entities: - User - Event

Each event belongs to one user through a foreign key relationship.

License

This project is intended for educational purposes.
