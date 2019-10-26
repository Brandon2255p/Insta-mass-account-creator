import pickle
import os
from .config import Config, ASSET_DIR
from ast import literal_eval
import logging

def list_created_account():
    file_path = ASSET_DIR + '/usernames.pkl'
    does_not_exist = not os.path.exists(file_path)
    if does_not_exist:
        return []
    with open(file_path, 'rb' ) as f:
        try:
            return pickle.load(f)
        except EOFError:
            return []
    return []
