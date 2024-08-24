import smtplib


class Config:
    def __init__(self):
        self.__bot_email = "botpham242001@gmail.com"
        self.__password = "zycbercxsxznwjuh"
        self.connection = smtplib.SMTP("smtp.gmail.com")
        self.connection.starttls()
        self.connection.login(user=self.__bot_email, password=self.__password)

    def send_mail(self, to_addr, text):
        self.connection.sendmail(from_addr=self.__bot_email, to_addrs=to_addr, msg=text)

    def connection_close(self):
        self.connection.close()