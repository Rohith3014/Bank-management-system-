import sqlite3

def connect():
    return sqlite3.connect("database/bank.db")

def init_db():
    conn = connect()
    cur = conn.cursor()
    # Accounts table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            acc_no TEXT PRIMARY KEY,
            name TEXT,
            pin TEXT,
            balance REAL,
            status TEXT
        )
    """)
    # Transactions table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            acc_no TEXT,
            type TEXT,
            amount REAL,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()