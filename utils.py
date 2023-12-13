import yagmail
import os
from dotenv import load_dotenv
load_dotenv()
email_address = os.getenv('EMAIL_ADDRESS')
email_password = os.getenv('EMAIL_PASSWORD')

def send(*args, **keargs):
    yag = yagmail.SMTP(
        email_address, 
        email_password, 
        host='smtp.163.com'
    )
    yag.send(*args, **keargs)
    
if __name__ == '__main__':
    send(
        to='80733866@qq.com',
        subject='test',
        contents='test'
    )