import os
import hashlib
from datetime import datetime

# ================== FILES ==================
ACCOUNT_FILE = "accounts.dat"
TRANS_FILE = "transactions.dat"

# ================== ADMIN ==================
ADMIN_USER = "admin"
ADMIN_PASS = "1234"

INTEREST_RATE = 0.05   # 5% interest


# ================== UTILITIES ==================
def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()


def init_storage():
    if not os.path.exists(ACCOUNT_FILE):
        open(ACCOUNT_FILE, "w").close()
    if not os.path.exists(TRANS_FILE):
        open(TRANS_FILE, "w").close()


def load_accounts():
    data = {}
    with open(ACCOUNT_FILE, "r") as f:
        for line in f:
            acc, name, pin, bal, status = line.strip().split("|")
            data[acc] = {
                "name": name,
                "pin": pin,
                "balance": float(bal),
                "status": status
            }
    return data


def save_accounts(data):
    with open(ACCOUNT_FILE, "w") as f:
        for acc, d in data.items():
            f.write(f"{acc}|{d['name']}|{d['pin']}|{d['balance']}|{d['status']}\n")


def log_transaction(acc, ttype, amount):
    with open(TRANS_FILE, "a") as f:
        f.write(f"{acc}|{ttype}|{amount}|{datetime.now()}\n")


# ================== APPLY ACCOUNT ==================
def apply_account():
    data = load_accounts()
    acc_no = str(1001 + len(data))

    name = input("Enter Name: ")
    pin = hash_pin(input("Create PIN: "))

    data[acc_no] = {
        "name": name,
        "pin": pin,
        "balance": 0.0,
        "status": "PENDING"
    }

    save_accounts(data)
    print("\n✔ Account request submitted")
    print("✔ Your Account Number:", acc_no)


# ================== ADMIN PANEL ==================
def admin_panel():
    u = input("Admin Username: ")
    p = input("Admin Password: ")

    if u != ADMIN_USER or p != ADMIN_PASS:
        print("❌ Invalid Admin Login")
        return

    data = load_accounts()

    print("\n--- PENDING ACCOUNTS ---")
    print(f"{'ACC NO':<10}{'NAME':<20}{'STATUS':<10}")
    print("-" * 40)

    pending = False
    for acc, d in data.items():
        if d["status"] == "PENDING":
            print(f"{acc:<10}{d['name']:<20}{d['status']:<10}")
            pending = True

    if not pending:
        print("No pending requests")

    acc = input("\nEnter account number to APPROVE (0 to exit): ")
    if acc in data and data[acc]["status"] == "PENDING":
        data[acc]["status"] = "ACTIVE"
        save_accounts(data)
        print("✔ Account Approved")


# ================== CUSTOMER LOGIN ==================
def customer_login():
    acc = input("Account Number: ")
    pin = hash_pin(input("PIN: "))

    data = load_accounts()

    if acc not in data:
        print("❌ Account not found")
        return

    if data[acc]["pin"] != pin:
        print("❌ Incorrect PIN")
        return

    if data[acc]["status"] != "ACTIVE":
        print("❌ Account not active")
        return

    customer_menu(acc, data)


# ================== CUSTOMER MENU ==================
def customer_menu(acc, data):
    while True:
        print("\n--- CUSTOMER DASHBOARD ---")
        print("1. Credit (Deposit)")
        print("2. Debit (Withdraw)")
        print("3. Balance Enquiry")
        print("4. Transaction History")
        print("5. Add Interest")
        print("6. Close Account")
        print("7. Logout")

        ch = input("Choose: ")

        if ch == "1":
            amt = float(input("Enter amount: "))
            data[acc]["balance"] += amt
            log_transaction(acc, "CREDIT", amt)
            save_accounts(data)
            print("✔ Amount Credited")

        elif ch == "2":
            amt = float(input("Enter amount: "))
            if amt > data[acc]["balance"]:
                print("❌ Insufficient balance")
            else:
                data[acc]["balance"] -= amt
                log_transaction(acc, "DEBIT", amt)
                save_accounts(data)
                print("✔ Amount Debited")

        elif ch == "3":
            print("Current Balance:", data[acc]["balance"])

        elif ch == "4":
            print("\n--- TRANSACTION HISTORY ---")
            found = False
            with open(TRANS_FILE, "r") as f:
                for line in f:
                    a, t, amt, dt = line.strip().split("|")
                    if a == acc:
                        print(f"{t:<8} | {amt:<10} | {dt}")
                        found = True
            if not found:
                print("No transactions")

        elif ch == "5":
            interest = data[acc]["balance"] * INTEREST_RATE
            data[acc]["balance"] += interest
            log_transaction(acc, "INTEREST", interest)
            save_accounts(data)
            print("✔ Interest Added:", interest)

        elif ch == "6":
            if input("Confirm close (yes/no): ").lower() == "yes":
                data[acc]["status"] = "CLOSED"
                save_accounts(data)
                print("✔ Account Closed")
                break

        elif ch == "7":
            print("✔ Logged Out")
            break

        else:
            print("Invalid option")


# ================== MAIN ==================
def main():
    init_storage()
    while True:
        print("\n=== BANK MANAGEMENT SYSTEM ===")
        print("1. Apply New Account")
        print("2. Customer Login")
        print("3. Admin Login")
        print("4. Exit")

        ch = input("Select: ")

        if ch == "1":
            apply_account()
        elif ch == "2":
            customer_login()
        elif ch == "3":
            admin_panel()
        elif ch == "4":
            print("Thank you for using our bank ")
            break
        else:
            print("Invalid choice")


main()