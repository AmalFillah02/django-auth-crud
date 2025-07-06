# Django Auth & CRUD User

Sebuah aplikasi berbasis Django yang memiliki fitur **Autentikasi Pengguna (Sign Up, Sign In, Sign Out)** dan fitur **CRUD (Create, Read, Update, Delete)** data pengguna. Proyek ini dibuat sebagai bagian dari assessment tes.

## ✨ Fitur

- 🔐 Autentikasi:
  - Sign Up
  - Sign In
  - Sign Out
- 👤 Manajemen Pengguna:
  - Daftar pengguna
  - Tambah pengguna
  - Edit pengguna
  - Hapus pengguna
- 🔒 Semua fitur CRUD hanya bisa diakses jika pengguna sudah login.
- ⚙️ Validasi form & feedback menggunakan Django messages

## 🛠️ Tech Stack

- Python 3
- Django 5
- SQLite (default DB)
- HTML & CSS

## 🚀 Cara Menjalankan

1. **Clone Repository**
   ```bash
   git clone https://github.com/AmalFillah02/django-auth-crud.git
   cd django-auth-crud
   ```
2. **Buat virtual environment & install depedensi**
   ```bash
   python -m venv env
   env\Scripts\activate # Windows
   pip install django
3. **Migrasi dan run**
   ```bash
   python manage.py migrate
   python manage.py runserver

## 👨‍💻 Author
Amal Fillah
