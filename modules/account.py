
""" author: feezyhendrix

    this module contains followers generation
 """

import random
import mechanicalsoup
import string
import logging

from .config import Config
from .getIdentity import User

from .mail_service import MailService

class Account(object):
    def __init__(self, user: User):
        self.name = user.name
        self.username = self._username_from_name(user.name)
        self.password = self._random_password()
        self.email = self._email_from_username(self.username)
        self.gender = user.gender
        self.birthday = user.birthday

    @staticmethod
    def _username_from_name(name):
        n = str(random.randint(1, 99))
        name = str(name).lower().replace(" ", "")
        username = name + n
        logging.info("Username: {}".format(username))
        return(username)

    @staticmethod
    def _random_password():
        password_characters = string.ascii_letters + string.digits
        return ''.join(random.choice(password_characters) for i in range(12))

    @staticmethod
    def _email_from_username(username):
        mail = MailService()
        email = mail.get_email_address(username)
        return email


def new_account() -> Account:
    user = User.new_random()
    return Account(user)
