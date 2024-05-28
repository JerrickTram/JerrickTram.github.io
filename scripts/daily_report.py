import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import sys

# Add the project directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models import Word

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def get_top_missed_words():
    return Word.query.order_by(Word.incorrect_count.desc()).limit(5).all()

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = os.getenv('MAIL_DEFAULT_SENDER')
    msg['To'] = os.getenv('MAIL_RECIPIENT')
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(os.getenv('MAIL_USERNAME'), os.getenv('MAIL_PASSWORD'))
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

with app.app_context():
    top_missed_words = get_top_missed_words()
    word_list = "\n".join([f"{word.swedish_word} - Missed {word.incorrect_count} times" for word in top_missed_words])
    user_name = os.getenv('USER_NAME')
    email_body = f"""
    Hi {user_name},

    Here are the top 5 most missed words from your Swedish learning sessions today:

    {word_list}

    Keep practicing to improve your accuracy!

    Best regards,
    Swedish Learning Tracker
    """
    send_email('Daily Report: Top 5 Most Missed Words', email_body)
