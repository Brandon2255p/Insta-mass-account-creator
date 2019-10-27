import mechanicalsoup
import random
import logging

logger = logging.getLogger("getRandomIdentity")


class User(object):
    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender

    @staticmethod
    def new_random():
        return User._getRandomIdentity()

    @staticmethod
    def _getRandomIdentity(country=None):
        gender = random.choice(["male", "female"])
        name_set = random.choice(["us", "en","fr", "it", "no"])
        country_list = random.choice(["au", "za", "uk", "us"])
        if country is not None:
            name_set = country
            country_list = country
        logger.info("Gender: {}".format(gender))
        URL = "https://fakenamegenerator.com/gen-{}-{}-{}.php".format(
            gender, name_set, country_list)
        logger.info("Url generated: {}".format(URL))
        browser = mechanicalsoup.StatefulBrowser(
            raise_on_404=True,
            user_agent='MyBot/0.1'
        )
        page = browser.get(URL)
        address_div = page.soup.find(
            "div",
            {"class": "address"}
        )
        completename = address_div.find(
            "h3"
        )

        extra_div = page.soup.find(
            "div",
            {"class": "extra"}
        )

        all_dl = page.soup.find_all(
            "dl",
            {'class': 'dl-horizontal'}
        )

        logger.info(
            f"Name: {completename.contents[0]}, Gener: {gender}")
        user = User(completename.contents[0], gender)
        return user
