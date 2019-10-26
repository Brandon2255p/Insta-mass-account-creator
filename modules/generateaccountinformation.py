
""" author: feezyhendrix

    this module contains followers generation
 """

import random
import mechanicalsoup
import string
import logging

from .config import Config
from .getIdentity import User


class Account(object):
    def __init__(self, user: User):
        self.name = user.name
        self.username = self._username(user.name)
        self.password = self._generatePassword()
        self.email = self._genEmail(self.username)
        self.gender = user.gender
        self.birthday = user.birthday

    @staticmethod
    def _username(identity):
        n = str(random.randint(1, 99))
        name = str(identity).lower().replace(" ", "")
        username = name + n
        logging.info("Username: {}".format(username))
        return(username)

    @staticmethod
    def _generatePassword():
        password_characters = string.ascii_letters + string.digits
        return ''.join(random.choice(password_characters) for i in range(12))

    @staticmethod
    def _genEmail(username):
        return ''.join(username + "@" + str(Config["email_domain"]))


def new_account() -> Account:
    user = User.new_random()
    return Account(user)
