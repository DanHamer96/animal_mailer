import smtplib
import pandas as pd
from email.message import EmailMessage
from dates import Dates
import imghdr


class SendEmail(object):

    def __init__(self):

        # get the details of the account we'll be sending the email from - these are stored in a csv locally
        self.fp = '/Users/dannyhamer96/login_details/dh_email/login.csv'
        self.data = pd.read_csv(self.fp)
        self.my_email = str(self.data.iloc[0]['value'])
        self.my_password = str(self.data.iloc[1]['value'])
        self.recipient_email = str(self.data.iloc[2]['value'])

        # misc
        self.day_today = Dates().get_dates()[1]
        self.msg = None

    def create_email(self, subject, content):

        # populate the email fields
        self.msg = EmailMessage()
        self.msg['Subject'] = subject
        self.msg['From'] = self.my_email
        self.msg['To'] = self.recipient_email
        self.msg.set_content(content)

        # add an image - corresponding image number to today's date
        file = '/Users/dannyhamer96/PycharmProjects/animal_mailer/images/img_%s.jpg' % self.day_today

        with open(file, 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name

        self.msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

        # format and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.my_email, self.my_password)

            smtp.send_message(self.msg)

# send the email
SendEmail().create_email('Picture of the day: ' + str(Dates().get_dates()[0]),
                         'Good Morning!')
