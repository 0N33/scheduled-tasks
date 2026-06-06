##################### Extra Hard Starting Project ######################

import os
# 1. Update the birthdays.csv
import pandas
import smtplib
import random

# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt

#-----------------------personal info---------------------------#
sender_email_adress = os.environ.get("sender_email_adress")
sender_password =  os.environ.get("sender_password")


now = dt.datetime.now()
now_month = now.month
now_day_date = now.day

try: 
    data = pandas.read_csv("./Birthday wisher/birthdays.csv")
except FileNotFoundError:
    print("No file as birthday.csv")

else:

    todays_data_row = data[(data.month == now_month) & (data.day == now_day_date)]

    if todays_data_row.empty:
        print("No birthdays today!")

    else:
        for (index,rows) in todays_data_row.iterrows():
            reciever_name = rows["name"]
            reciever_email = rows.email


            random_file_number = random.randint(1,3)

            try:
                with open(f"./Birthday wisher/letter_templates/letter_{random_file_number}.txt", "r") as letter:
                    letter_content = letter.read()
                    final_content = letter_content.replace("[NAME]", reciever_name)

                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=sender_email_adress,password=sender_password)
                    connection.sendmail(from_addr=sender_email_adress,
                                        to_addrs=reciever_email,
                                        msg=f"Subject:Happy Birthday {reciever_name}!!!\n\n{final_content}"
                                        )

            except FileNotFoundError:
                print("No file found!\nNot continuing")






