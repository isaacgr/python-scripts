import smtplib
import os
import imghdr
from email.message import EmailMessage

EMAIL = os.environ.get('EMAIL')
PASS = os.environ.get('PASS')

message = EmailMessage()
message['Subject'] = 'Test'
message['From'] = EMAIL
message['To'] = EMAIL

message.set_content('This is a test')

with open('test_image.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

message.add_attachment(file_data, maintype='image',\
    subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:

    s.login(EMAIL, PASS)

    s.send_message(message)


# to setup a localhost server, use the below
# python3 -m smtpd -c DebuggingServer -n localhost:6969


