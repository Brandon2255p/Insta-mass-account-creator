from .config import Config, ASSET_DIR
import logging
import pickle
from .list_created_account import list_created_account

def store(account):
    accounts = list_created_account()
    accounts.append(account)
    with open(ASSET_DIR + '/usernames.pkl', 'wb') as f:
        logging.info("Storing username {}".format(str(account['username'])))
        logging.info(str(account))
        pickle.dump(account, f, pickle.HIGHEST_PROTOCOL)
