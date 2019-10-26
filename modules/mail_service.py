import json
import os
import pickle
from ast import literal_eval

from dotenv import find_dotenv, load_dotenv
from tempMail2 import TempMail

from config import ASSET_DIR

load_dotenv(find_dotenv())

api_key = os.getenv("TEMPMAIL_API_KEY")
tm = TempMail(api_key=api_key)
emails = tm.get_mailbox("filomenasagese49@dmailpro.net")
if 'error' in emails:
    print ('No mail!')
with open(ASSET_DIR + '/mailbox.pickle', 'wb') as f:
    mailbox = pickle.dump(emails, f, protocol=pickle.HIGHEST_PROTOCOL)

with open(ASSET_DIR + '/mailbox.pickle', 'rb') as f:
    mailbox = pickle.load(f)
    regisrtation = [mail['mail_text']
                    for mail in mailbox if "registrations@mail.instagram.com" in mail['mail_from']]
    for mail in regisrtation:
        print(mail)
