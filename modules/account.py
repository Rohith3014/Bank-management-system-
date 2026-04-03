from database.db import connect
from utils.security import hash_pin

def create_account(name, pin):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM accounts")
    acc_no = str(1001 + cur.fetchone()[0])
    cur.execute("INSERT INTO accounts VALUES (?, ?, ?, ?, ?)",
                (acc_no, name, hash_pin(pin), 0.0, "PENDING"))
    conn.commit()
    conn.close()
    print("✔ Account created! Account Number:", acc_no)