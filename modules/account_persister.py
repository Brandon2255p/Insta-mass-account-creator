import logging
from shutil import copyfile
import os
import json
from ast import literal_eval

from .config import ASSET_DIR, Config
from .account import Account, account_from_dictionary

file_path = ASSET_DIR + '/usernames.txt'

logging.basicConfig(level=logging.DEBUG)
def list_created_account():
    does_not_exist = not os.path.exists(file_path)
    if does_not_exist:
        return []
    with open(file_path, 'r') as file_handle:
        f = '"' + file_handle.read() + '"'
        try:
            accounts =  eval(json.loads(f))
            accounts = [account_from_dictionary(acc) for acc in accounts]
            return accounts
        except EOFError:
            return []
    return []



def store_all(accounts):
    acc_model = [acc.__dict__ for acc in accounts]
    # Saving the dictionary
    with open(file_path, 'w') as file_handle:
        file_handle.write(str(acc_model))

def store(new_account):
    file_path = ASSET_DIR + '/usernames.pkl'
    accounts = list_created_account()
    accounts.append(new_account)
    store_all(accounts)



if __name__ == "__main__":
    for acc in list_created_account():
        print(acc)