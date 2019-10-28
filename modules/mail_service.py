import json
import os
import pickle
import random
from ast import literal_eval
from time import sleep

import requests
from dotenv import find_dotenv, load_dotenv
from tempMail2 import TempMail

from .config import ASSET_DIR

class MailService(object):
    def __init__(self):
        load_dotenv(find_dotenv())
        api_key = os.getenv("TEMPMAIL_API_KEY")
        self.mailer: TempMail = TempMail(api_key=api_key)

    def get_email_address(self, username: str) -> str:
        domain = random.choice(self.mailer.available_domains)
        return f"{username}{domain}"

    def wait_for_mail(self, email_address: str, timeout: int) -> str:
        total_wait = 0
        while total_wait < timeout:
            sleep_time = 2
            sleep(sleep_time)
            total_wait += sleep_time
            mailbox = self.mailer.get_mailbox(email=email_address)
            registration = [mail['mail_text'] for mail in mailbox if "registrations@mail.instagram.com" in mail['mail_from'] or 'Confirm your email address for Instagram' in mail['mail_subject']]
            if len(registration) > 0:
                return registration[len(registration) -1]
