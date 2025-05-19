#  Polytechnic Library Management System 

> `Team Name: SPI-EliteCoders ~(Sylhet Polytechnic Institute)`

> The Polytechnic Library Management System is a web-based solution primarily developed for Library Administrators to efficiently manage library operations such as book inventory, student membership, book issuing, and returns. It also facilitates controlled student access, ensuring accountability and streamlined management.



####  *– Contributors*
> Backend Engineers :  | `AN Mamun` <br> 
> Frontend Engineers:  | `Amit`, `Wazid`, `Sami`, `Mustofa`, `Abdullah`, `Pracurjo`
---

### 🎯 System Purpose
- To simplify the responsibilities of the library administrator
- To digitize and automate manual library tasks
- To allow students to create accounts, request books, and track borrow history
- To provide a secure and verified onboarding process for students

##  👥 User Roles

##### 1. Administrator
<h6> 
 
- Full access to the system
- Verify new student accounts
- Add/update/delete books
- Track issued/returned books
- Manage fines and overdue alerts

</h6>

#####  2. Student

<h6>
 
- Can register an account (inactive by default)
- Must be approved by the admin before access
- Once approved, can:
- Browse available books
- Borrow books (based on borrowing rules)
- Return books
- View personal borrow history

<h6> 


### 🔐 User Onboarding Flow
> **Student Registration**: - Student signs up and submits their personal and academic information. <br> 
> **Admin Verification**: - Admin reviews the student data and activates the account upon approval. <br> 
> **Access Granted**: - Once activated, students can log in and use the library system (borrow, return, search books, etc.) <br> 

### 🛠️ Key Features 	Description
<h6>
 
- Student Registration	Students register and wait for admin approval
- Admin Panel	Admin dashboard to manage books and student accounts
- Book Management	Add, edit, delete, and categorize books
- Borrow & Return	Issue and return books, track deadlines
- Fine Calculation	Automatic fine generation for late returns
- Borrowing History	Students and admins can view borrowing logs
- Search & Filter	Quickly search books by name, author, category, etc.

</h6>

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
| PUT    | `/dashboard/active_student/<int:pk>/activate/`| Activate a student by ID (admin only) |  [Example](#activate-a-student-by-id)|
| PUT    | `/dashboard/active_student/<int:pk>/delete/` | Delete a student by ID (admin only) |  [Example](#delete-a-student-by-id)|


### 🔍 Available Student Query Parameters (Filters)

You can filter GET requests to endpoints , using the following query parameters:

`?role=student` , `?phone=017XXXXXXXX`, `?email=user@example.com`, `?registration=123456`,  `?department=CSE`, `?session=20-21`, `?nationality_type=NID`, `?nationality_number=1234567890`, 

<br>


---

## 📎 Live API Docs

View API schema and test endpoints via Spectacular UI:

🔗 [Swagger UI](http://localhost:8000/api/schema/swagger-ui/)  
🔗 [ReDoc UI](http://localhost:8000/api/schema/redoc/) *(Update links based on deployment)*

--- 



## 🛡️ Authentication

All protected endpoints require token-based authentication.  
Use the following header format:

```http
Authorization: Token <your_token_here>
```




##  Register a new user
```json
{ 
  "username": "string", unique
  "full_name": "string",
  "password": "string", 
  "email": "string", unique
  "phone": "string", unique 
  "roll": "string", unique 
  "registration": "string", unique
  "session": "string", 
  "department": "string",
  "address": "string",
  "nationality_type": "nid/birth",
  "nationality_number": "string", unique
  "role": "student/admin"
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

## Delete a student by ID

```json
{
  "token_id": "string"
}
```
