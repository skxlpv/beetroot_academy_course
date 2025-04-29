# 🚀 DRF + Aiogram Project

A Python backend combining **Django REST Framework** for API development and **Aiogram** for building an asynchronous Telegram bot using `asyncio`.

---

## 📂 Project Structure
```
beetroot_academy_course/
│
├── bot/                    # Telegram bot (Aiogram)
│   ├── handlers/
│   ├── middlewares/
│   ├── services/
│   └── main.py             # Bot entry point
│
├── api/                    # Django project
│   ├── manage.py
│   ├── api/                # Django core
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── app1/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   │
│   └── app2/
│       └── (same structure)
│
│
├── venv/
├── .env
├── requirements.txt
└── README.md
```
## ⚙️ Requirements
- Python 3.10+
- PostgreSQL (or preferred database)
- Telegram Bot API token

---

## 📥 Installation

### 1️⃣ Clone the repository:
```bash
git clone https://github.com/skxlpv/beetroot_academy_course.git
cd beetroot_academy_course
```

### 2️⃣ Create & activate a virtual environment:
```bash
python -m venv .venv
venv\Scripts\activate    # Windows
source venv/bin/activate   # Linux/MacOS
```

### 3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables:
Create a `.env` file in the project root:
```
DEBUG=True
SECRET_KEY=your_django_secret_key
DATABASE_USER=database_owner
DATABASE_PASSWORD=database_password
DATABASE_HOST=database_host
DATABASE_PORT=database_port
TELEGRAM_TOKEN=your_telegram_bot_token
```

### 5️⃣ Apply database migrations:
```bash
python manage.py migrate
```

### 6️⃣ Run the Django development server:
```bash
python manage.py runserver
```

---

## 🤖 Running the Telegram Bot
Ensure your Django server is running and then start the bot:
```bash
python bot/main.py
```

---

## 📡 API Endpoints
Base URL:
```
http://127.0.0.1:8000/api/
```

Example endpoints (in progress):
```
/api/users/        # User management
/api/another_app/  # Additional app routes
```

---

## 🛠️ Project Commands
| Command                             | Description             |
|-------------------------------------|-------------------------|
| `python manage.py runserver`        | Run Django server       |
| `python bot/main.py`                | Start Telegram bot      |
| `python manage.py createsuperuser`  | Create admin user       |
| `python manage.py makemigrations`   | Create migration files  |
| `python manage.py migrate app zero` | Undo migrations for app |

---

## 📌 Useful Links
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Aiogram Documentation](https://docs.aiogram.dev/)
- [Asyncio](https://docs.python.org/3/library/asyncio.html)

---