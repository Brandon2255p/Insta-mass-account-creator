import json
import os
import pickle
from ast import literal_eval
import random
from dotenv import find_dotenv, load_dotenv
from tempMail2 import TempMail

from .config import ASSET_DIR


# emails = tm.get_mailbox("filomenasagese49@dmailpro.net")
# if 'error' in emails:
#     print ('No mail!')
# with open(ASSET_DIR + '/mailbox.pickle', 'wb') as f:
#     mailbox = pickle.dump(emails, f, protocol=pickle.HIGHEST_PROTOCOL)

# with open(ASSET_DIR + '/mailbox.pickle', 'rb') as f:
#     mailbox = pickle.load(f)
#     regisrtation = [mail['mail_text']
#                     for mail in mailbox if "registrations@mail.instagram.com" in mail['mail_from']]
#     for mail in regisrtation:
#         print(mail)


class MailService(object):
    def __init__(self):
        load_dotenv(find_dotenv())
        api_key = os.getenv("TEMPMAIL_API_KEY")
        self.mailer: TempMail = TempMail(api_key=api_key)

    def get_email_address(self, username: str) -> str:
        domain = random.choice(self.mailer.available_domains)
        # ''.join(username + "@" + str(Config["email_domain"]))
        return f"{username}{domain}"

    def wait_for_mail(self, email_address: str, timeout: int) -> str:
        total_wait = 0
        while total_wait < timeout:
            sleep_time = 2
            sleep(sleep_time)
            total_wait += sleep_time
            mailbox = self.mailer.get_mailbox(email=email_address)
            registration = [mail['mail_text'] for mail in mailbox if "registrations@mail.instagram.com" in mail['mail_from']]
            if len(registration) > 0:
                return registration[len(registration) -1]
