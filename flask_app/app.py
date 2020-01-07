from flask import Flask
from flask import render_template
from flask_mail import Mail
from flask_mail import Message


app = Flask(__name__)

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'youremail@gmail.com',
    MAIL_PASSWORD = 'yourpassword',

))

mail = Mail(app)

def sendEmail():
    # send an email to gmail with the alert that the alarm was triggered
    msg = Message("Your alarm has been TRIGGERED!!!!....Yikes >:(",
                sender=("Arduino Alarm", "brokeninto@gmail.com"),
                recipients=["youremail@gmail.com"])
    msg.html = "<b>Alert</b> <h3>your alarm was set off</h3> <p> you should be worried...</p>"
    mail.send(msg)


@app.route('/')
def start():
    return "you are at the start route"

@app.route('/alarmtriggered')
def trigger_data_display(package="default"):
    sendEmail()
    return "an email alert has been sent to you!"

@app.route('/<name>')
def pages(name="you"):
    return render_template("index.html",name_to_use=name)

app.run(debug=True, port = 3000, host = '0.0.0.0')
