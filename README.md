# 🔐 PassVault - Password Manager Web App

A secure, full-stack password manager web application built with Django.

## ✨ Features

- 🔐 **Secure Authentication** - Login/Register system
- 🔑 **Encrypted Storage** - All passwords encrypted using Fernet encryption
- ➕ **Add Passwords** - Save passwords with categories
- 👁 **View/Hide** - Toggle password visibility
- ✏️ **Update** - Edit existing passwords
- 🗑 **Delete** - Remove passwords with confirmation
- 🔍 **Search** - Find passwords by website name
- 💡 **Password Generator** - Suggests strong random passwords
- 🎨 **Dark UI** - Clean professional dark theme

## 🛠 Tech Stack

- **Backend** - Django 5.2
- **Database** - SQLite
- **Encryption** - Fernet (cryptography library)
- **Frontend** - Bootstrap 5 + Custom CSS
- **Auth** - Django built-in authentication
- **Deployment** - Render

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

1. Clone the repo:
```bash
git clone https://github.com/SimranSajid/PassVault.git
cd PassVault
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
SECRET_KEY=your-secret-key-here
DEBUG=True

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run server:
```bash
python manage.py runserver
```

8. Open browser:
http://127.0.0.1:8000

## 🔒 Security Features

- Fernet encryption for all stored passwords
- Django CSRF protection
- Session timeout after 30 minutes
- HTTP-only cookies
- Clickjacking protection
- Environment variables for secrets

## 📁 Project Structure : 
PassManagerWeb/
├── passmanager/
│   ├── settings.py
│   └── urls.py
├── vault/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── encryption.py
│   ├── templates/
│   └── static/
├── requirements.txt
├── Procfile
└── manage.py

## ⚠️ Note

This app stores passwords locally. Keep your secret.key and db.sqlite3 safe — never share them publicly.

## 👩‍💻 Author

**Simran Sajid**
- GitHub: [@SimranSajid](https://github.com/SimranSajid)

## 📄 License

This project is for educational purposes.
