import imaplib
import getpass,os
m = imaplib.IMAP4_SSL('imap.gmail.com')

email = os.environ.get('EMAIL', '')
passwd = os.environ.get('PASSWORD', '')
m.login(email, passwd)
m.list()
m.select('INBOX')
print(m.select('INBOX'))
#typ, data = m.search(None,'FROM azal88*')
#print(data)
# not done yet have to work on it````