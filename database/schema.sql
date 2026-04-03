-- Create Accounts Table
CREATE TABLE IF NOT EXISTS accounts (
    acc_no TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    pin TEXT NOT NULL,
    balance REAL DEFAULT 0.0,
    status TEXT DEFAULT 'PENDING'
);

-- Create Transactions Table
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    acc_no TEXT,
    type TEXT CHECK(type IN ('CREDIT', 'DEBIT')),
    amount REAL NOT NULL,
    date TEXT,
    FOREIGN KEY (acc_no) REFERENCES accounts(acc_no)
);