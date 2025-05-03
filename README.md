# Employer Management System API

## Features
### Custom User Authentication
- User registration with email and password
- Login to obtain JWT tokens
- Retrieve the logged-in user's profile

### Employer Management
- Create, retrieve, update, and delete employers
- Each employer is linked to a specific user
- Users can only manage their own employers

### Token-Based Authentication
- Uses JWT for secure authentication
- Access protected endpoints with a Bearer token


## Installation
### Install Dependencies:
pip install -r requirements.txt

### Apply Migration 
python manage.py makemigrations
python manage.py migrate

### Run Server
python manage.py runserver


## Postman API Testing Collection
### Sign up:
- Send a POST request to "/api/auth/signup/" with the following body:
{
    "email": "test@example.com",
    "password": "password123"
}
### Login:
- Send a POST request to "/api/auth/login/" with the following body:
{
    "email": "test@example.com",
    "password": "password123"
}
- Copy the access token from the response.
- Include the token in the Authorization header for all protected endpoints:
  - Authorization: Bearer <access_token>
### Create an Employer:
- Send a POST request to "/api/employers/" with the following body:
{
    "company_name": "Softvence",
    "contact_person_name": "Angel",
    "email": "angel@email.com", 
    "phone_number": "321456987",
    "address": "412 Street, Test Road"
}
### Employers List:
- Send a GET request to "/api/employers/"
### Update or Delete Employer:
- Use the "/api/employers/<id>/" endpoint with the appropriate HTTP method (PUT, or DELETE).
