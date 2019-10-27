import logging
from modules.config import Config
from modules.seleniumbot import runbot
from modules.requestbot import runBot

logging.basicConfig(level=logging)

def accountCreator():
    if Config['bot_type'] == 1:
        runbot()
    else:
        runBot()


accountCreator()

