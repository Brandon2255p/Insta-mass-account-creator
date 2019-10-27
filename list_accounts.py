from modules.account_persister import list_created_account 
from modules.account import Account

accounts = list_created_account()

for account in accounts:
    print(f"ACCOUNT: {account}")
