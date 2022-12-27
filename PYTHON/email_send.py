import smtplib
import getpass,os,logging

logging.basicConfig(filename="app_log.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)
 
# Test messages
# logger.debug("Harmless debug Message")

# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")


smtp_object= smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()
#passwd=input('whats your passwd?: ')
sender_address = os.environ.get('EMAIL', '')
sender_pass = os.environ.get('PASSWORD', '')
smtp_object.login(sender_address, sender_pass)
from_address=sender_address
to_address= 'azal88@gmail.com'#input('enter reciever email address: ')
subject = 'Test Subject'#input('enter your subject line: ')
message = 'Test Message!'#input('enter your message body: ')
msg = 'subject: '+ subject+'\n' + message
smtp_object.sendmail(from_address, to_address,msg)
logger.info(f'{sender_address} send to {to_address} with {subject}.')
