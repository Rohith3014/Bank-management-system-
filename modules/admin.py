from database.db import connect

ADMIN_USER = "admin"
ADMIN_PASS = "1234"

def admin_login(username, password):
    if username != ADMIN_USER or password != ADMIN_PASS:
        print("❌ Invalid Admin Login")
        return

    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT acc_no, name, status FROM accounts WHERE status='PENDING'")
    pending = cur.fetchall()
    if not pending:
        print("No pending requests")
    else:
        for acc, name, status in pending:
            print(acc, name, status)

    acc_to_approve = input("Enter account number to approve (0 to skip): ")
    if acc_to_approve != "0":
        cur.execute("UPDATE accounts SET status='ACTIVE' WHERE acc_no=?", (acc_to_approve,))
        conn.commit()
        print("✔ Account Approved")
    conn.close()