from database.db import connect
from utils.security import hash_pin
from modules.transactions import log_transaction, show_transactions

def customer_login(acc_no, pin):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT pin, balance, status FROM accounts WHERE acc_no=?", (acc_no,))
    row = cur.fetchone()
    if not row:
        print("❌ Account not found")
        return
    stored_pin, balance, status = row
    if hash_pin(pin) != stored_pin:
        print("❌ Incorrect PIN")
        return
    if status != "ACTIVE":
        print("❌ Account not active")
        return

    print("✔ Login successful")

    while True:
        choice = input("1.Deposit 2.Withdraw 3.Balance 4.Transactions 5.Exit: ")
        if choice == "1":
            amt = float(input("Amount to deposit: "))
            cur.execute("UPDATE accounts SET balance = balance + ? WHERE acc_no=?", (amt, acc_no))
            log_transaction(acc_no, "CREDIT", amt)
        elif choice == "2":
            amt = float(input("Amount to withdraw: "))
            if amt > balance:
                print("❌ Insufficient funds")
            else:
                cur.execute("UPDATE accounts SET balance = balance - ? WHERE acc_no=?", (amt, acc_no))
                log_transaction(acc_no, "DEBIT", amt)
        elif choice == "3":
            cur.execute("SELECT balance FROM accounts WHERE acc_no=?", (acc_no,))
            print("Balance:", cur.fetchone()[0])
        elif choice == "4":
            show_transactions(acc_no)
        elif choice == "5":
            break
        conn.commit()
    conn.close()