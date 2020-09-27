import imaplib
import getpass
m = imaplib.IMAP4_SSL('imap.gmail.com')

email = getpass.getpass('please enter your email: ')
passwd = getpass.getpass('please enter your password: ')
m.login(email, passwd)
m.list()
m.select('INBOX')
#print(m.select('inbox'))
typ, data = m.search(None,'FROM user ')
print(data)
# not done yet have to work on it