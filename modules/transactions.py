from database.db import connect
from datetime import datetime

def log_transaction(acc_no, ttype, amount):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO transactions (acc_no, type, amount, date) VALUES (?, ?, ?, ?)",
                (acc_no, ttype, amount, str(datetime.now())))
    conn.commit()
    conn.close()

def show_transactions(acc_no):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT type, amount, date FROM transactions WHERE acc_no=?", (acc_no,))
    rows = cur.fetchall()
    if not rows:
        print("No transactions")
    else:
        for t, amt, dt in rows:
            print(f"{t:<8} | {amt:<10} | {dt}")
    conn.close()