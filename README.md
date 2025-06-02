#  Polytechnic Library Management System 

> `Team Name: SPI-EliteCoders ~(Sylhet Polytechnic Institute)`

> The Polytechnic Library Management System is a web-based solution primarily developed for Library Administrators to efficiently manage library operations such as book inventory, student membership, book issuing, and returns. It also facilitates controlled student access, ensuring accountability and streamlined management.



####  *– Contributors*
> Developted Engineers :  | `AN Mamun` <br>  
---
 
 
<h3> 
  
[  <code> Frontend Live </code>](https://spi-library.vercel.app/) [ <code> Fontend GitHub </code>](https://github.com/anmamun0/spi-library)  [ <code> Backend Live </code>](https://spi-library.onrender.com/)  [ <code> Backend GitHub </code>](https://github.com/anmamun0/polytechnic-library-system-Backend) 

</h3>

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

## 🔐 Authentication APIs

| Method | Endpoint             | Description            | Example |
|--------|----------------------|------------------------|---------|
| POST   | `/user/register/`    | Register a new user (get-notification)     |  [Example](#register-a-new-user)|
| POST   | `/user/login/`       | Login and receive token|  [Example](#login-and-receive-token)|
| POST   | `/user/logout/`      | Logout and delete token|  [Example](#logout-and-delete-token)|


 
## Profile APIs Endpoints

This API is designed for admin users to manage user profiles securely via Token authentication.

##### 🔐 Token Authentication

For all endpoints, admin authentication is required using the token via:

###### If you're using JavaScript fetch, just set the headers like |  For JWT Authentication

```js
headers: {
  'Content-Type': 'application/json',
  'Authorization': 'Token ecb093d6304e1ce411b7cbfabeb4f44a846e08d8'
}
```
 

| Method | Endpoint                             | Description                    | Example |
|--------|--------------------------------------|--------------------------------|---------|
| GET    | `/user/profile/`                     | Get all active profiles        | [Example](#get-all-active-profiles) |
| GET    | `/user/profile/unactive/`            | Get all inactive profiles(admin)      | [Example](#get-inactive-profiles) |
| POST   | `/user/profile/`                     | Create a new profile (admin)           | [Example](#create-profile) |
| PUT    | `/user/profile/<pk>/`                | Fully update a profile (admin)         | [Example](#update-profile) |
| PATCH  | `/user/profile/<pk>/`                | Partially update a profile (admin)     | [Example](#partial-update-profile) |
| DELETE | `/user/profile/<pk>/`                | Delete a profile (admin)               | [Example](#delete-profile) |
| POST   | `/user/profile/<pk>/activate/`       | Activate a deactivated profile (admin)(get-notification)  | [Example](#activate-profile) |


##### Filters Tags:
###### `?role=student` , `?phone=017XXXXXXXX`, `?email=user@example.com`, `?registration=123456`,  ` department=CSE`, `?session=20-21`, `?nationality_type=NID`, `?nationality_number=1234567890`, 



##  Books APIs Endpoints

| Method | Endpoint        | Description                      |
|--------|------------------|----------------------------------|
| GET    | `/book/books/`         | Get all books                    |
| POST   | `/book/books/`         | Create a new book (admin)        | 
| PUT    | `/book/books/<pk>/`    | Fully update a book (admin)      |
| PATCH  | `/book/books/<pk>/`    | Partially update a book (admin)  |
| DELETE | `/book/books/<pk>/`    | Delete a book (admin)            |


##### Filters tags: 
######   `title`,`author`, `isbn`, `language`, `category__name`


## Categories APIs Endpoints 

| Method | Endpoint            | Description                          | 
|--------|---------------------|--------------------------------------| 
| GET    | `/category/`        | Get all categories                   | 
| GET    | `/category/<pk>/`   | Get a specific category              | 
| POST   | `/category/`        | Create a new category (admin)        | 
| PUT    | `/category/<pk>/`   | Fully update a category (admin)      | 
| PATCH  | `/category/<pk>/`   | Partially update a category (admin)  | 
| DELETE | `/category/<pk>/`   | Delete a category (admin)            | 


## 📚 Transaction APIs Endpoints

| Method | Endpoint                 | Description                                                                 |
|--------|--------------------------|-----------------------------------------------------------------------------|
| GET    | `/transaction/`          | Get all transactions (admin token), or only the user's transactions (user token) |
| GET    | `/transaction/<pk>/`     | Get a specific transaction (admin or the related user)                     |
| POST   | `/transaction/`          | Create a new transaction request (authenticated user only)                 |
| PATCH  | `/transaction/<pk>/`     | Admin-only: Update transaction to 'borrowed' status if book is available   |
| DELETE | `/transaction/<pk>/`     | Admin-only: Delete a transaction                                            |

##### Filter Tags:
###### `profile`, `book__title`, `status`,`due_date`,`request_date`,`borrow_date`,`return_date`

 
### 🔍 Available Student Query Parameters (Filters)

You can filter GET requests to endpoints , using the following query parameters:


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
  "blood": "string",
  "gender":"MALE/FEMALE",
  "birthday":"Date",
  "nationality_type": "NID/BIRTH",
  "nationality_number": "string", unique
  "role": "student/admin" // Default - student
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
 

 ## Profile 

```json
    {
        "id": 1,
        "user": "anmamun0",
        "full_name": "Nur Mohummod Al Mamun",
        "role": "admin",
        "email": "almamun20044@gmail.com",
        "phone": "01782059949",
        "roll": "676229",
        "registration": "1502221113",
        "session": "2122",
        "address": "Sylhet, Bangladesh - Bangladesh",
        "blood": "O+",
        "nationality_type": "birth",
        "nationality_number": "12345678909876543"
    }
```

 ## Category
```json
{
        "id": 1,
        "name": "Python Programming-hero",
        "slug": "python-programming"
    }
```


 ## Category model
 
 ```json
{
    "id": 1,
    "category": [],
    "image": "https://anmamun0.vercel.app/",
    "title": "Updated -2",
    "author": "hero",
    "isbn": "01",
    "language": "Bangla",
    "description": "asdf",
    "copies": 10,
    "available": 3
}
 ```


 ## Transaction Model

 ```json
  {
    "id": 0,
    "profile": "string",
    "request_date": "2025-05-24T20:41:41.172Z",
    "due_date": 3,
    "borrow_date": "2025-05-24T20:41:41.172Z",
    "return_date": "2025-05-24",
    "status": "pending",
    "book": 0
  }
 ```