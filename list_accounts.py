from modules import list_created_account

accounts = list_created_account.list_created_account()

for account in accounts:
    print(f"username {account['username']}\tpassword {account['password']}")
