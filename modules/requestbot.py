"""

"""
import requests
from modules.config import Config
from modules.account import new_account, Account
import json
import re
from modules.account_persister import store
import logging

#custom class for creating accounts
class CreateAccount:
    def __init__(self, account : Account, use_custom_proxy : bool, use_local_ip_address : bool, proxy=None):
        self.logger = logging.getLogger("CreateAccountRequests")
        self.sockets = []
        self.email = account.email
        self.username = account.username
        self.password = account.password
        self.name = account.name
        self.use_custom_proxy = use_custom_proxy
        self.use_local_ip_address = use_local_ip_address
        self.url = "https://www.instagram.com/accounts/web_create_ajax/"
        self.referer_url = "https://www.instagram.com/"
        self.proxy = proxy
       

    # A function to fetch custom proxies
    def __collect_sockets(self):
        r = requests.get("https://www.sslproxies.org/")
        matches = re.findall(r"<td>\d+.\d+.\d+.\d+</td><td>\d+</td>", r.text)
        revised_list = [m1.replace("<td>", "") for m1 in matches]
        for socket_str in revised_list:
            self.sockets.append(socket_str[:-5].replace("</td>", ":"))

    # def __collectcrsf(self):
    #     r = requests.get('https://instagram.com/accounts/emailsignup/')
    #     print(r)

    # Account creation function
    def createaccount(self):
        # Account creation payload
        payload = {
            'email': self.email,
            'password': self.password,
            'username': self.username,
            'first_name': self.name,
           'seamless_login_enabled' : '1',
            'tos_version' : 'row',
            'opt_into_one_tap' : 'false'
        }

        """
            Check if to use local ip address to create account, then create account based on the amount set in the config.py
        """
        if self.use_local_ip_address is True:
            self.logger.info("Using local IP")
            session = requests.Session()
            try: 
                session_start = session.get(self.url);
                session.headers.update({'referer' : self.referer_url,'x-csrftoken' : session_start.cookies['csrftoken']})

                create_request = session.post(self.url, data=payload, allow_redirects=True)
                session.headers.update({'x-csrftoken' : session_start.cookies['csrftoken']})
                response_text = create_request.text
                response = json.loads(create_request.text)
                self.logger.debug(response)
            except Exception as e:
                self.logger.error(e)
                self.logger.error("---Request Bot --- An error occured while creating account with local ip address")

        elif self.use_custom_proxy is True:
            self.logger.info("Using custom proxy")
            try: 
                session = requests.Session()
                if(self.proxy is not None):
                    try: 
                        session_start = session.get(self.url,   proxies={'http' : self.proxy, 'https' : self.proxy})
                        session.headers.update({'referer' : self.referer_url,'x-csrftoken' : session_start.cookies['csrftoken']})

                        create_request = session.post(self.url, data=payload, allow_redirects=True)
                        session.headers.update({'x-csrftoken' : session_start.cookies['csrftoken']})
                        response_text = create_request.text
                        response = json.loads(create_request.text)
                        self.logger.debug(response)
                    except Exception as e:
                        self.logger.error(e)
                        self.logger.error("---Request Bot --- An error occured while creating account with custom proxy")
                else: 
                    raise Exception('---Request Bot --- Proxy must to added to proxies.txt list')

                session.get(self.url)
            except Exception as e:
                self.logger.error(e)
                self.logger.error("---Request Bot --- An error occured while creating account with custom proxy")
        else:
            self.__collect_sockets()
            if len(self.sockets) > 0:
                self.logger.info("Using proxy list")
                current_socket = self.sockets.pop(0)
                self.logger.info(f"Current proxy {current_socket}")
                proxies = {"http": "http://" + current_socket, "https": "https://" + current_socket}
                session = requests.Session()
                try:
                    session_start = session.get(self.url,   proxies=proxies);
                    session.headers.update({'referer' : self.referer_url,'x-csrftoken' : session_start.cookies['csrftoken']})

                    create_request = session.post(self.url, data=payload, allow_redirects=True)
                    session.headers.update({'x-csrftoken' : session_start.cookies['csrftoken']})
                    response_text = create_request.text
                    response = json.loads(create_request.text)
                    self.logger.debug(response)
                except Exception as e:
                    self.logger.error(e)
                    self.logger.error("---Request Bot --- An error occured while creating account with fetched proxy")


def runBot():
    for i in range(Config['amount_of_account']):
        account_info = new_account()
        if(Config['use_custom_proxy'] == True):
             with open(Config['proxy_file_path'], 'r') as file:
                content = file.read().splitlines()
                for proxy in content:
                    account = CreateAccount(
                        account_info,
                        Config['use_custom_proxy'], 
                        Config['use_local_ip_address'],proxy=proxy)
                    account.createaccount()
        else :
            logging.info(account_info)
            account = CreateAccount(
                account_info,
                Config['use_custom_proxy'], 
                Config['use_local_ip_address'])
            account.createaccount()
