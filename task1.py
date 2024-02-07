from celery import Celery
import smtplib, ssl

app = Celery('celery_', broker='redis://localhost:6379/0')

emails = ['tursunovhojiakbar27@gmail.com', 'usmonovsalokhiddin@gmail.com',
          'shohjahonobruyev3@gmail.com', 'ibodullofayzullayev2001@gmail.com',
          'askarbekyusufboyev@gmail.com', 'abdulaziz.abdusattorov05@gmail.com',
          'ominanuriddinova2212@gmail.com', 'shoxdiyor04@gmail.com',
          'elboyashurov187@gmail.com', 'yunusovabdulmajid@gmail.com',
          'uznext@gmail.com', 'toepammiddle@gmail.com']


@app.task
def send_email(emails: list):
    for user in emails:
        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = "shoxdiyor04@gmail.com"
        receiver_email = user
        password = "oakf yxhd vhnn fzoe"
        message = """\
        Subject: Bu birinchi task.

        This message is sent from Python."""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
