import datetime as dt
import pandas as pd
import random
import smtplib

from main import MY_EMAIL,PASSWORD


today = (dt.datetime.now().month,dt.datetime.now().day)
#(1,26)
df = pd.read_csv("birthdays.csv")


new_dict = {(row["month"],row["day"]) : row for (index,row) in df.iterrows()}
#(1,26)

if today in new_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as f:
        letter = f.read()
        letter = letter.replace("[NAME]",new_dict[today]["name"])

        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=new_dict[today]["email"],
                msg=f"Subject:HAPPY BIRTHDAY\n\n{letter}"
            )