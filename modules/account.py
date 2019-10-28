
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
    def __init__(self, name: str, username: str, password: str, email: str, gender: str):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.gender = gender
    def __repr__(self):
        return f"{self.name}\t{self.username}\t{self.password}\t{self.email}"

def _from_user(user: User):
    username = _username_from_name(user.name)
    email = _email_from_username(username)
    new_acc = Account(name = user.name,
        username = username,
        password = _random_password(),
        email = email, 
        gender = user.gender)
    return new_acc
        
def account_from_dictionary(user: dict):
    new_acc = Account(name = user['name'],
    username = user['username'],
    password = user['password'],
    email = user['email'],
    gender = user['gender'])
    return new_acc


def _username_from_name(name):
    n = str(random.randint(1, 99))
    name = str(name).lower().replace(" ", "")
    username = name + n
    return(username)

def _random_password():
    password_characters = string.ascii_letters + string.digits
    return ''.join(random.choice(password_characters) for i in range(12))

def _email_from_username(username):
    mail = MailService()
    email = mail.get_email_address(username)
    return email


def new_account() -> Account:
    user = User.new_random()
    return _from_user(user)
