import logging
from shutil import copyfile
import os
import pickle
from ast import literal_eval

from .config import ASSET_DIR, Config
from .account import Account

logging.basicConfig(level=logging.DEBUG)
def list_created_account():
    file_path = ASSET_DIR + '/usernames.pkl'
    does_not_exist = not os.path.exists(file_path)
    if does_not_exist:
        return []
    with open(file_path, 'rb' ) as f:
        try:
            accounts =  pickle.load(f)
            return accounts
        except EOFError:
            return []
    return []



def store_all(accounts):
    file_path = ASSET_DIR + '/usernames.pkl'
    copyfile(file_path, file_path + '.bak')
    with open(file_path, 'wb') as f:
        pickle.dump(accounts, f, pickle.HIGHEST_PROTOCOL)


def store(new_account):
    file_path = ASSET_DIR + '/usernames.pkl'
    accounts = list_created_account()
    accounts.append(new_account)
    store_all(accounts)



if __name__ == "__main__":
    for acc in list_created_account():
        print(acc)