# 🛒 Full-Stack E-Commerce Platform

A fully functional **e-commerce web application** built with:

- **Backend:** Django & Django REST Framework (DRF)
- **Frontend:** Quasar Framework (Vue.js)
- **Database:** PostgreSQL (or your DB of choice)
- **Authentication:** JWT-based auth (secure login/register)
- **Admin:** Django Admin for product and order management

---

## 🚀 Features

- 🔐 User registration, login, and JWT authentication  
- 🛍️ Product listing with categories, filtering, and search  
- 📄 Product detail view with image gallery  
- 🛒 Shopping cart with quantity management  
- 💳 Checkout with address and order summary  
- 📦 Order placement and order history  
- 🧾 Admin dashboard using Django Admin  
- 📱 Responsive UI with modern Quasar components  

---

## 🧩 Tech Stack

| Layer       | Technology                   |
|-------------|------------------------------|
| Frontend    | [Vue.js](https://vuejs.org/) + [Quasar](https://quasar.dev/) |
| Backend     | [Django](https://www.djangoproject.com/) + [Django REST Framework](https://www.django-rest-framework.org/) |
| Database    | PostgreSQL / SQLite          |
| Auth        | JSON Web Tokens (JWT)        |
| Styling     | Tailwind CSS (optional)      |

---

## 📦 How to Run

### Backend (Django)

```bash
cd backend/
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


cd frontend/
yarn install
yarn quasar dev


/backend     → Django project with DRF API  
/frontend    → Quasar (Vue) frontend app
