# Welcome to my alx-project-nexus - E-Commerce Backend!
-------------

# Overview of the ProDev Backend Engineering Program
-------------

The ProDev Backend Engineering program is a comprehensive learning journey designed to equip participants with advanced backend development skills. Through a series of milestones, including the comprehensive Airbnb Project, learners master 'PYTHON', 'Django', database design, API development, and deployment strategies. Project Nexus serves as the capstone, allowing me to apply these skills to a real-world e-commerce backend system, showcasing technical expertise and readiness for professional opportunities.

This repository serves as a documentation hub for their major learnings from the ProDev Backend Engineering program. This repository will showcase their understanding of backend engineering concepts, tools, and best practices.

## Tech stack
------------

Python 3.10+

Django 4.x

Django REST Framework

djangorestframework-simplejwt (JWT auth)

PostgreSQL 13+

Swagger/OpenAPI (drf-spectacular or drf-yasg)

Gunicorn + Nginx for deployment

### 1. Clone repo

git clone <https://github.com/sodex4real11/alx-project-nexus>

cd repo

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

#### 2. Configure .env (example variables in .env.example):

DEBUG=False

SECRET_KEY=your-secret

DATABASE_URL=postgres://user:password@host:port/dbname

ALLOWED_HOSTS=your-domain.com

### 3. Run migrations and create superuser

python manage.py migrate

python manage.py createsuperuser

#### 4. Run Locally

python manage.py runserver

#### 5. API docs

Swagger UI: /api/docs/

OpenAPI JSON: /api/schema/
