from flask import Flask, render_template, session, request, redirect, url_for, make_response, flash
#from flask_sqlalchemy import SQLAlchemy
#from flask_mail import Mail, Message
import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#import hashlib
from flask_mail import Mail, Message
#from random import *
#import config
from form import SignUp



app = Flask(__name__)

submiters = []

# #app.debug = True
# app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'thecode'
#
# app.secret_key = 'key'
# #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost/flask_app_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)



app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSl'] = False
app.config['MAIL_USERNAME'] = ''  # введите свой адрес электронной почты здесь
app.config['MAIL_DEFAULT_SENDER'] = ''  # и здесь
app.config['MAIL_PASSWORD'] = ''  # введите пароль

mail = Mail(app)


# msg = Message("Subject", recipients=['recipient_1@example.com'])
# msg.body = 'cactibi shop'
# mail.send(msg)
#
#
#
# @app.route('/contact/', methods=['get', 'post'])
# def contact():
#     db.session.commit()
#     msg = Message("Feedback", recipients=[app.config['MAIL_USERNAME']])
#     msg.body = "You have received a new feedback from {} <{}>."
#     mail.send(msg)
#
#     print("\n Data received. Now redirecting ...")



@app.route('/')
def home():
    return 'Сейчас все будет'


@app.route('/index/')
def index():
    return render_template('index.html', success=False, error=False)


@app.route('/landing')
def landing():
    posts = [{'title': 'Flowers'}]
    return render_template('front.html', visits=66776, form=SignUp())


@app.route('/landing/<string:landing_id>')
def landingpost(landing_id):
    return 'Landing page' + landing_id


@app.route('/signup')
def signup():
    form = SignUp()

    return render_template('signup.html', form=form)


@app.route('/visits-count')
def visits():
    if 'visits' in session:
        session['visit'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return 'Total visits: {}'.format(session.get('visits'))


@app.route('/cookie/')
def cookie():
    if not request.cookies.get('foo'):
        res = make_response("Setting a cookie")
        res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    else:
        res = make_response("Value of cookie foo is {}".format(request.cookies.get('foo')))
    return res


@app.route('/send', methods=['POST'])
def send():
    email = request.form.get('email')

    message = 'You have subscribed to our email newsletters'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your email', 'password')
    server.sendmail('elisaveta.veev@gmail.com', email, message)

    if not email:
        error_statement = 'Form field required'
        return render_template('front.html')
    return render_template('email.html', success=False, error=False)


#база

#class Products(db.Model):
#    __tablename__ = 'Products'
#    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
#    name = db.Column(db.Text, nullable=False)
#    price = db.Column(db.Integer, nullable=False)
#    image = db.Column(db.Text, nullable=False)
#    stock = db.Column(db.Integer, nullable=False)

#class User(db.Model):
    #__tablename__ = "User"
    #id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #name = db.Column(db.Text, nullable=False)
    #password = db.Column(db.Text, nullable=False)
    #email = db.Column(db.Text, unique=True, nullable=False)
    #auth = db.Column(db.Integer, nullable=False)


#class Cart(db.Model):
    #__tablename__ = 'Cart'
    #id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #products_id = db.Column(db.Integer, db.ForeignKey('Products.id'))
    #quanity = db.Column(db.Integer, nullable=False)

#class Order(db.Model):
#  __tablename__ = "Order"
#    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#   user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
#    product_id = db.Column(db.Integer, db.ForeignKey('Products.id'))
#    datetime = db.Column(db.Text, nullable=False)
#    amount = db.Column(db.Integer, nullable=False)
#auth = False
#logged_in = False
#the_user = ""


if __name__ == "__ maim__":
    app.run(debug=True)
app.run()


