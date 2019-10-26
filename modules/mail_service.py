from tempMail2 import TempMail
from config import ASSET_DIR
import json
from ast import literal_eval
import pickle

# tm = TempMail(api_key='')
# emails = tm.get_mailbox("filomenasagese49@dmailpro.net")
# print(emails)
with open(ASSET_DIR + '/mailbox.pickle', 'rb' ) as f:
    mailbox = pickle.load(f)
    regisrtation = [mail['mail_text'] for mail in mailbox if "registrations@mail.instagram.com" in mail['mail_from']]
    for mail in regisrtation:

        print(mail)