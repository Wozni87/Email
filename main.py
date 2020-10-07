from email.message import EmailMessage
import smtplib
import csv


# Lets pull the email's from an external file
filename = 'email_list.csv'

with open(filename, 'r') as f:
    email_list = tuple(csv.reader(f, delimiter=' '))

#time to send the email!
for i in email_list:
    email = EmailMessage()
    email['from'] = 'My Python Email Script'
    email['to'] = i
    email['subject'] = 'Hello! '

    email.set_content('Just wanted to say Hi from Python!')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        try:
            smtp.login('Youremail@youremail.com', 'Your Password')
            smtp.send_message(email)
            print('Sent!')
        except:
            print('Well looks like login failed... may want to check that')