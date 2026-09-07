import smtplib
from email.message import EmailMessage
msg = EmailMessage()
msg['Subject'] = 'Proposal for vinayaka Chavithi'
msg['From'] = 'dhanushshivajim@gmail.com'
msg['To'] = 'vishnuvardhanroyal4@gmail.com'
msg.set_content('''
Dear Vishnu,
Greetings from Dhanush!
I hope this email finds you well. I am writing to propose a collaboration for the upcoming Vinayaka Chavithi festival.
I believe that our combined efforts can create a memorable experience for the community
Best regards,
Dhanush Shivaji''')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('dhanushshivajim@gmail.com','dykhnrpuurpqpstz')
server.send_message(msg)
print("Email sent successfully!")
server.quit()