import os
import stripe
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payment.db'
app.config['SECRET_KEY'] = 'secret_key'
app.config['STRIPE_SECRET_KEY'] = 'stripe_secret_key'
app.config['STRIPE_PUBLISHABLE_KEY'] = 'stripe_publishable_key'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'email@gmail.com'
app.config['MAIL_PASSWORD'] = 'email_password'

stripe.api_key = app.config['STRIPE_SECRET_KEY']

db = SQLAlchemy(app)
mail = Mail(app)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    payment_method = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(100), nullable=False)

    def __init__(self, user_id, payment_method, amount, status):
        self.user_id = user_id
        self.payment_method = payment_method
        self.amount = amount
        self.status = status

    def __repr__(self):
        return f'Payment({self.id}, {self.user_id}, {self.payment_method}, {self.amount}, {self.status})'

@app.route('/payment', methods=['POST'])
def make_payment():
    try:
        data = request.get_json()
        user_id = data['user_id']
        payment_method = data['payment_method']
        amount = data['amount']
        payment = Payment(user_id, payment_method, amount, 'pending')
        db.session.add(payment)
        db.session.commit()
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            source=payment_method,
            description='Test Charge'
        )
        if charge.status == 'succeeded':
            payment.status = 'succeeded'
            db.session.commit()
            msg = Message('Payment Successful', sender='email@gmail.com', recipients=[data['email']])
            msg.body = 'Your payment has been successful'
            mail.send(msg)
            return jsonify({'message': 'Payment successful'}), 200
        else:
            payment.status = 'failed'
            db.session.commit()
            return jsonify({'message': 'Payment failed'}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500
