# 📝 Django Todo App

A clean, minimal, and responsive **Todo List web application** built with Django.

This app allows users to register, log in, add, complete, and delete tasks — all with a beautiful UI.

---

## 🚀 Features

- User Registration & Login (with email, phone, and DOB)
- Password Change & Logout
- Add, complete, and delete tasks
- Task list with nice UI and completion toggle
- Custom authentication views (no Django forms)
- CSRF-protected, mobile-friendly interface

---

## 🖼️ UI Preview

![image](https://github.com/user-attachments/assets/04e77b97-f999-4343-ba72-edd97cf8d05d)


---

## 🛠️ Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS (inline), Google Fonts
- **Database**: MySQL (default for development)

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/django_task.git
cd django_task

Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

 Install Dependencies

python manage.py makemigrations
python manage.py migrate


 Start Development Server
python manage.py runserver

