from modules.mail_service import MailService
from modules.account_persister import list_created_account
import requests
import re
mailer = MailService()

accounts = list_created_account()[-1:]


for line in lines:
    url = re.search("(?P<url>https?://[^\s\]]+)", line).group("url")
    session = requests.Session()
    session_start = session.get(url)
    # print(line)
for account in accounts:
    email = mailer.wait_for_mail(email_address=account.email, timeout=10)
    lines = [line for line in email.splitlines(True) if 'confirm_email' in line][:1]
    for line in lines:
        url = re.search("(?P<url>https?://[^\s\]]+)", line).group("url")
        session = requests.Session()
        session_start = session.get(url)
