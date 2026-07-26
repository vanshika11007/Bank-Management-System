# 🏦 Bank Management System

A command-line **Bank Management System** developed using **Python**, **Object-Oriented Programming (OOP)**, and **MySQL**. The application provides a secure banking simulation where users can register, log in, and perform essential banking operations such as checking their balance, depositing money, withdrawing funds, and updating their password.

This project demonstrates how Python can be integrated with a relational database to build a real-world CRUD application while following object-oriented programming principles.

---

## 📖 Overview

The Bank Management System is a console-based application that manages user accounts using a MySQL database. Every registered user can securely access their account after authentication and perform basic banking transactions.

The project focuses on database connectivity, user authentication, and implementing banking functionalities using Python classes and methods.

---

## ✨ Features

- 👤 User Registration
- 🔐 Secure Login Authentication
- 💰 Balance Inquiry
- 💵 Deposit Money
- 💸 Withdraw Money
- 🔑 Change Password
- 🗄️ MySQL Database Integration
- 🧩 Object-Oriented Programming (OOP)
- 📟 Interactive Command-Line Interface

---

## 🛠️ Technologies Used

- Python 3.x
- MySQL
- MySQL Connector/Python
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```
Bank-Management-System/
│
├── bank.py              # Main application
├── README.md
└── bank_db.sql          # Database script (optional)
```

---

## 🗄️ Database

The application uses a MySQL database named:

```
bank_db
```

Example table structure:

| Column | Description |
|---------|-------------|
| account_no | Unique Account Number |
| name | Customer Name |
| email | Customer Email |
| password | Customer Password |
| balance | Current Account Balance |

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Bank-Management-System.git
```

### Move into the Project Folder

```bash
cd Bank-Management-System
```

### Install Required Package

```bash
pip install mysql-connector-python
```

### Create the Database

Create a MySQL database named:

```sql
CREATE DATABASE bank_db;
```

Create the user table:

```sql
CREATE TABLE user(
    account_no INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    balance DECIMAL(10,2) DEFAULT 0
);
```

### Configure Database Credentials

Update the following values in the Python file:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="bank_db"
)
```

### Run the Program

```bash
python bank.py
```

---

## 📋 Functionalities

### Registration

- Create a new bank account
- Stores user information in MySQL
- Generates an account number automatically

### Login

- Authenticate users using email and password

### Dashboard

After login, users can:

- Check Balance
- Deposit Money
- Withdraw Money
- Change Password
- Exit the application

---

## 🧠 OOP Concepts Used

- Classes
- Objects
- Constructors (`__init__`)
- Instance Variables
- Methods
- Encapsulation

---

## 🗃️ Database Operations

The project performs the following SQL operations:

- INSERT
- SELECT
- UPDATE
- Authentication using parameterized queries
- Database transactions using `commit()`

---

## 🔒 Security

- Uses parameterized SQL queries (`%s`) to help prevent SQL injection.
- Login is required before accessing banking operations.

> **Note:** Passwords are currently stored as plain text. In a production application, passwords should be hashed using libraries such as `bcrypt`.

---

## 🚀 Future Enhancements

- Password hashing (bcrypt)
- Money transfer between users
- Transaction history
- Account deletion
- Admin panel
- PIN authentication
- Email verification
- Interest calculation
- GUI using Tkinter or PyQt
- Logging system
- Exception-specific error handling

---

## 📚 What I Learned

- Python Object-Oriented Programming
- MySQL Database Connectivity
- CRUD Operations
- User Authentication
- SQL Parameterized Queries
- Exception Handling
- Console-Based Application Development

---

## 📄 License

This project is created for educational purposes and learning Python, OOP, and MySQL integration.

---

## 👩‍💻 Author

**Vanshika Kumawat**

If you found this project helpful, feel free to ⭐ the repository.
