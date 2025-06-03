
CollegeAPI is a RESTful API designed to manage and retrieve information related to colleges, departments, courses, and students. Built with Python, it serves as a backend solution for educational institutions to handle their data efficiently.

This project implements JWT Authentication in a Django Rest Framework (DRF) application for secure user login, registration, and protected API endpoints.


📚 Features

    User registration with password hashing

    User login and JWT token generation (access + refresh tokens)

    Token refresh endpoint

    Protected APIs with JWT authentication

    Logout by blacklisting tokens (optional)

    Built using Simple JWT (recommended)

🛠️ Tech Stack

    Backend: Django, Django Rest Framework (DRF)

    Authentication: Simple JWT

    Testing : Postman api

    Database:  (PostgreSQL)

🚀 Getting Started
Prerequisites

    Python 3.8+

    Django 5.5x

    pip (Python package manager)

    Virtual environment (recommended)
Installation

1:Clone the repository
    [git clone ](https://github.com/prabeshkhatiwada29/collegeapi.git)
    
    cd django-collegeapi
    
2:Set up a virtual environment
    python -m venv env
    
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    
3:Install dependencies

    pip install -r requirements.txt
    
4:Apply migrations:

     python manage.py migrate
     








  

    


