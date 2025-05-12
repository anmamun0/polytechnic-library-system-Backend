#  Polytechnic Library Management System 

> `Team Name: Amity of SPI (Sylhet Polytechnic Institute)`

> This project is a full-stack web application for user registration, authentication, and student management — designed for admin and student roles. It supports both frontend and backend separation and provides REST APIs secured with JWT tokens.

> Backend Engineers :  | `AN Mamun` <br> 
> Frontend Engineers:  | `Amit`, `Wazid`, `Sami`, `Mustofa`, `Abdullah`, `Pracurjo`
---

##   Tech Stack

####   Backend: 
 
- **`Django`** – Powerful Python web framework
- **`Django REST Framework (DRF)`** – Build RESTful APIs quickly
- **`JWT Authentication`** – Secure token-based authentication
- **`drf-spectacular`** – Automatic API schema/documentation generation
- **`PostgreSQL`** – Production-ready relational database


####   Frontend:
- **`React.js`** – Dynamic frontend development
- **`Tailwind CSS`** – Modern utility-first CSS styling
- **`Supabase`** – Open source Firebase alternative (for storage or auth if used)

---

# 📘 API Documentation

This project provides authentication and admin dashboard APIs using Django REST Framework.

---

> 🔐 Authentication APIs

| Method | Endpoint             | Description            | Example |
|--------|----------------------|------------------------|---------|
| POST   | `/user/register/`    | Register a new user    |  [Example](#register-a-new-user)|
| POST   | `/user/login/`       | Login and receive token|  [Example](#login-and-receive-token)|
| POST   | `/user/logout/`      | Logout and delete token|  [Example](#logout-and-delete-token)|

---

## 🛠️ Admin Dashboard APIs

> 🔒 Admin-only access
> 
| Method | Endpoint                                      | Description                          | Example |
|--------|-----------------------------------------------|--------------------------------------|---------|
| GET    | `/dashboard/pending_student/`                 | List of pending (inactive) students  | Just View| 
| GET    | `/dashboard/active_student/`                  | List of active students              | Just View| 
| PUT    | `/dashboard/active_student/<int:pk>/activate/` | Activate a student by ID (admin only) |  [Example](#activate-a-student-by-id)|

---

## 📎 Live API Docs

View API schema and test endpoints via Spectacular UI:

🔗 [Swagger UI](http://localhost:8000/api/schema/swagger-ui/)  
🔗 [ReDoc UI](http://localhost:8000/api/schema/redoc/) *(Update links based on deployment)*

---

👨‍💻 Team
🧠 Backend Engineer
- AN Mamun  – Facebook

🎨 Frontend Engineers
- Amit
 - Wazid
-  Mustofa
-  Abdullah
-  Pracurjo



## 🛡️ Authentication

All protected endpoints require token-based authentication.  
Use the following header format:

```http
Authorization: Token <your_token_here>
```




##  Register a new user
```json
{ 
  "username": "string",
  "full_name": "string",
  "password": "string",
  "email": "string",
  "phone": "string",
  "roll": "string",
  "registration": "string",
  "session": "stri",
  "address": "string",
  "nationality_type": "birth",
  "nationality_number": "string",
  "role": "student"
} 
```

## Login and receive token

```json
{
  "username": "string",
  "password": "string"
}
```

## Logout and delete token
```json
{
  "token_id": "string"
}
```

## Activate a student by ID

```json
{
  "token_id": "string"
}
```