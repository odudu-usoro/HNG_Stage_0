notepad README.md
🚀 Stage 0 Task – Dynamic Profile Endpoint
👤 Author

Name: Oduduabasi Usoro
Email: yakndarausoro1@gmail.com

Stack: Python/Django

📄 Project Overview

This project implements a RESTful API endpoint that returns my profile information along with a dynamic cat fact fetched from an external API (https://catfact.ninja/fact).

It was developed as part of the HNG Backend Internship – Stage 0 Task.

🧩 Features

Returns JSON-formatted profile data

Fetches a new cat fact dynamically from a public API on every request

Includes a UTC timestamp in ISO 8601 format

Implements proper error handling for external API requests

Fully deployed and accessible online

📡 API Endpoint

Base URL:
https://hngstage0-production-8607.up.railway.app

GET /me → Returns a JSON response:

{
  "status": "success",
  "user": {
    "email": "yakndarausoro1@gmail.com",
    "name": "Oduduabasi Usoro",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-19T14:31:25.659360+00:00",
  "fact": "Your cat's heart beats at a rate almost double that of yours."
}

⚙️ Technologies Used

Python 3.12

Django 3.2

Gunicorn

Requests

Railway (for deployment)

🧰 Installation & Setup (Local)

Clone the repository

git clone https://github.com/odudu-usoro/HNG_Stage_0.git
cd HNG_Stage_0


Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate   # on Windows


Install dependencies

pip install -r requirements.txt


Run the server

python manage.py runserver


Access locally

http://127.0.0.1:8000/me

⚙️ Environment Variables
Variable	Description	Example
DEBUG	Enables debug mode	True
🚀 Deployment

This app is deployed on Railway using:

Procfile for Gunicorn process definition

runtime.txt specifying Python version

requirements.txt for dependency installation

🧠 What I Learned

How to build and expose RESTful API endpoints in Django

How to consume and handle responses from third-party APIs

How to prepare Django apps for production deployment

How to deploy Django projects using Railway

🌍 Live Demo

🔗 Visit Live API Endpoint

✅ Status

Stage 0 task completed successfully.