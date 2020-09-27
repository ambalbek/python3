import smtplib
import getpass
smtp_object= smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()
#passwd=input('whats your passwd?: ')
email = getpass.getpass('Email: ')
passwd = getpass.getpass('password please: ') #nujen app password
smtp_object.login(email, passwd)
from_address=email
to_address=input('enter reciever email address: ')
subject = input('enter your subject line: ')
message = input('enter your message body: ')
msg = 'subject: '+ subject+'\n' + message
smtp_object.sendmail(from_address, to_address,msg)
