from twilio.rest import Client
import pandas as pd
import smtplib
from data_manager import DataManager

DF = pd.read_csv("~/data_ggr_scripts/data.csv")
MY_EMAIL = list(DF["my_email"])[0]
TARGET_EMAIL = list(DF["target_email"])[0]
PASSWORD = list(DF["password"])[0]

data_email = pd.read_csv["~/data_ggr_scripts/lesson_39.txt"]

class NotificationManager:

    def __init__(self):
        self.account_data = pd.read_csv("~/data_ggr_scripts/lesson_39.txt")
        self.account_sid = self.account_data["account_sid"]
        self.auth_token = self.account_data["auth_token"]
        self.client = Client(self.account_sid, self.auth_token)
        self.df_login = pd.read_csv("~/data_ggr_scripts/data.csv")
        self.my_email = list(self.df_login["my_email"])[0]
        self.target_email = list(self.df_login["target_email"])[0]
        self.password = list(self.df_login["password"])[0]

    def notification(self, info: dict):
        connections = ' ,'.join(info['connections'])
        if len(info["connections"]) != 0:
            message = self.client.messages \
                .create(body=f"\n\nPreço baixo para {info['cityTo']}!\n\nValor de R$ {info['lowest_price']}\n\nVoo com conexões em {connections} e duração de {info['duration']}\n\nCorre que dá tempo",
                        from_=data_email["my_phone"],
                        to=data_email["target_phone"])
        else:
            message = self.client.messages \
                .create(
                body=f"\n\nPreço baixo para {info['cityTo']}!\n\nValor de R$ {info['lowest_price']}\n\nSem conexões e duração de {info['duration']}\n\nCorre que dá tempo\n\nAcesse: {info['link']}",
                from_=data_email["my_phone"],
                to=data_email["target_phone"])

    def send_emails(self, info):
        connections = ' ,'.join(info['connections'])

        data_manager = DataManager()
        contacts = data_manager.get_contact_info()

        for i in contacts:
            msg = f"Subject:Flight Deals\n\nPrezado(a) {i['lastName']}\n\nPreco baixo para {info['cityTo'].encode('UTF-8')}!\n\n" + \
                  f"Valor de {info['lowest_price']} BRL\n\nCom {info['stops']} " + \
                  f"conexoes em {connections.encode('UTF-8')} duracao de {info['duration']}\n\n" + \
                  f"Corre que da tempo\n\nAcesse: {info['link']}"
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.password)
                connection.sendmail(from_addr=self.my_email,
                                    to_addrs=i["email"],
                                    msg=msg)
        print("Email enviado")
