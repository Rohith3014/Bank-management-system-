from database.db import init_db
from modules.account import create_account

# Initialize database
init_db()

print("=== BANK PROJECT DAY 1 ===")
name = input("Enter your name: ")
pin = input("Enter a PIN: ")
create_account(name, pin)