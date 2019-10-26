import pickle
from .config import Config, ASSET_DIR
from ast import literal_eval
import logging

def list_created_account():
    accounts = []
    with open(ASSET_DIR + '/usernames.pkl', 'rb' ) as f:
        try:
            accounts = pickle.load(f)
        except EOFError:
            pass

    return(accounts)
