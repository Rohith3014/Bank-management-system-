🏦 Bank Management System (Python)

A simple Bank Management System built using Python with file handling.
This project allows customers to create accounts, perform transactions, and administrators to approve accounts.

---

🚀 Features

👤 Customer Features

- Apply for new account
- Secure PIN (SHA256 hashing)
- Deposit money (Credit)
- Withdraw money (Debit)
- Balance enquiry
- Transaction history
- Add interest (5%)
- Close account
- Logout

🛠 Admin Features

- Admin login authentication
- View pending account requests
- Approve customer accounts

---

📂 Files Used

- "accounts.dat" → Stores account details
- "transactions.dat" → Stores transaction history

Both files are automatically created when the program runs.

---

🔐 Default Admin Login

Username: "admin"
Password: "1234"

---

🧠 How It Works

1. Customer applies for account
2. Account status is PENDING
3. Admin approves account
4. Customer logs in
5. Customer performs banking operations

---

▶️ How to Run

Make sure Python is installed, then run:

python bank.py

---

📋 Menu Options

Main Menu

1. Apply New Account
2. Customer Login
3. Admin Login
4. Exit

---

💰 Interest

- Interest Rate: 5%
- Applied manually using "Add Interest" option

---

🔒 Security

- PIN stored using SHA256 hashing
- Account status control (PENDING / ACTIVE / CLOSED)

---

🧾 Example Transaction Record

1001|CREDIT|5000|2026-04-03 14:22:11
1001|DEBIT|1000|2026-04-03 14:25:02

---

🛠 Technologies Used

- Python
- File Handling
- Hashlib (Security)
- Datetime

---
