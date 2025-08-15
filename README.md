# Django Form Project

## 📌 Overview
This project is a simple Django application demonstrating the creation, validation, and submission of a form using Django’s built-in **`forms`** module.

The project is built as part of **Module 14: Django – Form Project** for the Python course.

---

## 🛠 Features
- Django project and app setup
- Form creation using Django `forms.Form`
- CSRF protection for secure submissions
- Basic form validation
- Displays success message after submission

---

## 📂 Project Structure

form_project/
│
├── form_project/ # Project configuration files
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
├── form_app/ # Django app
│ ├── forms.py # ContactForm definition
│ ├── views.py # Form handling logic
│ ├── urls.py # App-level URL routes
│ └── templates/
│ └── contact.html # Form HTML template
│
└── manage.py # Django management script


---

## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/django-form-project.git
cd django-form-project
```
### 2. Create Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate       # On Windows

pip install django

### 3. Run Migrations
```
python manage.py migrate
```
### 4. Start the Development Server
```
python manage.py runserver
```

### 5. Open in Browser
```
http://127.0.0.1:8000/
```








