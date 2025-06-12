# 🚀 Linktree Backend with Referral System  

A Django REST API that supports user authentication (JWT), referral tracking, and a reward system.

---

## 🛠 Features
✅ **User Authentication (JWT-based Login & Registration)**

✅ **Referral System** (Users can register with a referral code)

✅ **User Profile API** (Get user details & referral count)

✅ **PostgreSQL Integration**

✅ **API Documentation with Swagger (`drf-spectacular`)**

✅ **Secure Rate Limiting (`django_ratelimit`)**

---

## 📌 Tech Stack
- **Django & Django REST Framework**
- **PostgreSQL** (via `psycopg`)
- **JWT Authentication** (`djangorestframework-simplejwt`)
- **API Docs** (`drf-spectacular`)
- **Rate Limiting** (`django_ratelimit`)

---

## 🚀 Installation Guide  

```bash

 🔹 1️⃣ Clone the Repository
 
git clone https://github.com/YOUR_GITHUB_USERNAME/linktree-backend.git
cd linktree-backend


🔹 2️⃣ Create a Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate  # On Mac/Linux
# On Windows use: venv\Scripts\activate

pip install -r requirements.txt


🔹 3️⃣ Configure Database
Open settings.py and configure PostgreSQL:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'linktree_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


Now, apply the migrations:

python manage.py makemigrations
python manage.py migrate


🔹 4️⃣ Create Superuser

python manage.py createsuperuser
Follow the prompts to create an admin account.

🔹 5️⃣ Run the Server

python manage.py runserver
Your API will be available at:
http://127.0.0.1:8000/

📜 API Documentation
Swagger UI available at:
🔹 http://127.0.0.1:8000/docs/
🔹 OpenAPI Schema: http://127.0.0.1:8000/schema/

📌 API Endpoints
🔹 User Authentication
Method	Endpoint	            Description
POST	/api/register/	        Register a new user
POST	/api/login/	            Login & get JWT tokens
POST	/api/token/refresh/	    Refresh JWT token


🔹 User Profile & Referrals
Method	    Endpoint	        Description
GET	        /api/profile/	    Get user details & referral count
GET	        /api/referrals/	    Get referred users