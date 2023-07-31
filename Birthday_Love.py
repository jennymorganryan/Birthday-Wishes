import datetime
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText

# Function to send text message
def send_text(receiver_number, message):
    # Provide your Twilio account SID, auth token, and phone number details here
    account_sid = 'AC360cb594b32784f176cd4580e4bda9c4'
    auth_token = '575bfdb154f0fd3aeaaf878d8f149ca1'
    twilio_number = '+18446061784'

    # Create Twilio client
    client = Client(account_sid, auth_token)

    # Send text message
    message = client.messages.create(
        body=message,
        from_=twilio_number,
        to=receiver_number
    )

    print(f"Sent text message to {receiver_number}.")

# Function to send email reminder
def send_email(receiver_email, subject, message):
    # Provide your email details here
    sender_email = 'testingemailmillion@gmail.com'
    sender_password = 'ajwe klol ddtm eelc'

    # Create email message
    email_message = MIMEText(message)
    email_message['Subject'] = subject
    email_message['From'] = sender_email
    email_message['To'] = receiver_email

    # Connect to SMTP server and send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(email_message)

    print(f"Sent email reminder to {receiver_email}.")

# Function to check and send birthday reminders
def send_birthday_reminders(contacts, receiver_email):
    today = datetime.date.today()
    one_day_before = today + datetime.timedelta(days=1)

    for name, contact in contacts.items():
        birthday = contact['birthday']
        if one_day_before.month == birthday.month and one_day_before.day == birthday.day:
            # Send email reminder to receiver_email
            subject = "Birthday Reminder"
            message = f"Hi, just a friendly reminder that {name}'s birthday is tomorrow! Make sure to wish them a happy birthday!"
            send_email(receiver_email, subject, message)

        if today.month == birthday.month and today.day == birthday.day:
            # Send birthday text message to friend
            message = f"Hi {name}! Happy birthday! I am so grateful to have you in my life. Have an amazing day!"
            send_text(contact['phone'], message)

# Prompt the user to input their email address
def prompt_receiver_email():
    return input("Enter your email address to receive birthday reminders: ")

# Prompt the user to input friend's details
def prompt_friend_details():
    name = input("Enter friend's name: ")
    birthday = input("Enter friend's birthday (YYYY-MM-DD): ")
    phone = input("Enter friend's phone number: ")

    return {
        'name': name,
        'birthday': datetime.datetime.strptime(birthday, '%Y-%m-%d').date(),
        'phone': phone
    }

# contacts dictionary with names, birthdays, and contact details
contacts = {}

# Prompt the user to add friends
while True:
    add_friend = input("Add a friend? (y/n): ")
    if add_friend.lower() == 'n':
        break

    friend_details = prompt_friend_details()
    contacts[friend_details['name']] = friend_details

receiver_email = prompt_receiver_email()
send_birthday_reminders(contacts, receiver_email)
