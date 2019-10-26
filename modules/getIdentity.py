import mechanicalsoup
import random
import logging

logger = logging.getLogger("getRandomIdentity")


def getRandomIdentity(country=None):
    gender = random.choice(["male", "female"])
    name_set = random.choice(["us", "ar", "au", "br", "celat", "ch", "zhtw", "hr", "cs", "dk", "nl", "en", "er", "fi", "fr", "gr", "gl",
                              "sp", "hobbit", "hu", "is", "ig", "it", "jpja", "jp", "tlh", "ninja", "no", "fa", "pl", "ru", "rucyr", "gd", "sl", "sw", "th", "vn"])
    country_list = random.choice(["au", "as", "bg", "br", "ca", "cyen", "cygk", "cz", "dk", "ee", "fi", "fr", "gr",
                                  "gl", "hu", "is", "it", "nl", "nz", "no", "pl", "pt", "sl", "za", "sp", "sw", "sz", "tn", "uk", "us", "uy"])
    if country is not None:
        name_set = country
        country_list = country
    logger.info("Gender: {}".format(gender))
    URL = "https://it.fakenamegenerator.com/gen-{}-{}-{}.php".format(
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

    birthday = all_dl[5].find("dd").contents[0]
    logger.info(
        f"Name: {completename.contents[0]}, Gener: {gender}, Birthday: {birthday}".format(birthday))

    return(completename.contents[0], gender, birthday)
