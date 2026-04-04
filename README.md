🏦** BANK MANAGEMENT SYSTEM**

Version 1 – File Handling

Version 2 – SQL (SQLite)

- A secure, user-friendly, and robust Bank Management System built using Python.
- 
This project simulates real-world banking operations for both customers and admins.
It was initially developed using File Handling (Version 1) and later enhanced with SQLite (Version 2) for better performance, reliability, and persistent storage.



**🌟 Why This Project?**

This project is perfect for:-

- Learning Python programming with practical applications
- Understanding data storage with files and databases
- Practicing security concepts (hashed PINs)
- Simulating a banking system workflow

  
**🚀 Features**


**👤 Customer Features**


- Open a new account easily and securely
- Secure PIN stored using SHA256 hashing for protection
- Deposit and withdraw money with ease
- Check account balance anytime
- View transaction history for transparency
- Earn interest (5%) on account balance
- Close account safely when needed
- Logout securely

  
**🛠 Admin Features**


- Admin login authentication
- View pending account requests
- Approve or reject customer accounts


**📁 Project Structure**


Bank-Management-System/
│
├── bank.py        # Version 1 (File Handling)
├── main.py        # Version 2 (SQLite)
├── accounts.dat   # Auto created
├── transactions.dat # Auto created
└── bank.db        # Auto created


**📂 Version 1 – File Handling**


- Stores account details in accounts.dat
- Stores transaction history in transactions.dat
- Files are automatically created when the program runs
- Simple and easy to understand for beginners
- Run Version 1:
  
-Bash:-
    python bank.py
⚠️ Best for learning file-based data management and basic banking workflows.


**🗄 Version 2 – SQL (SQLite)**

- Uses SQLite database to store accounts and transactions
- Database is automatically created on first run
- Provides faster, reliable, and persistent data storage
- Supports real-world banking simulation with proper data management
- Run Version 2:
  
- Bash:-
     python main.py
⚡ Ideal for production-level projects and professional practice.


**🔐 Default Admin Login**


- Username: admin
- Password: 1234
💡 You can change these credentials in the code for enhanced security.


**🔒 Security**


- PINs are securely hashed using SHA256
- Account status controlled: PENDING / ACTIVE / CLOSED
- Only approved accounts can perform transactions
- Transaction timestamps are recorded for accountability

  
**🛠 Technologies Used**


- Python – Core programming language
- File Handling – For Version 1 data storage
- SQLite (SQL) – For Version 2 database storage
- Hashlib – For secure PIN hashing
- Datetime – For transaction timestamping
