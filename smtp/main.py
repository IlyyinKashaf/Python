import pandas as pd 
import random 
import smtplib 
from datetime import *  

email = 'testingmaail1234@gmail.com'
password = 'fxyqnwzydocvtdha'



now = datetime.now()
today = (now.month,now.day)

try:
    data = pd.read_csv('smtp/birthdays.csv')
    birthday_dict = {(data_row['month'],data_row['day']):data_row  for (index,data_row) in data.iterrows()}
    if today in birthday_dict:
        birthday_person = birthday_dict[today]
        recipient = birthday_person['email']
        files = f'smtp/letter_templates/letter_{random.randint(1,3)}.txt'
        with open(files) as letter:
            content = letter.read()
            content = content.replace('[Name]',birthday_person['name'])
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(email, password)
            message = f"Subject: Happy Birthday!\n\n{content}"
            server.sendmail(email, recipient, message)

   
except FileNotFoundError as f:
    print('cannot open')







