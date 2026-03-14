from flask import Blueprint, jsonify
from stripe_payment import app, db

routes = Blueprint('routes', __name__)

@routes.route('/payment', methods=['POST'])
def make_payment():
    return app.make_payment()

@routes.route('/payment/history', methods=['GET'])
def payment_history():
    payments = Payment.query.all()
    return jsonify([{'id': payment.id, 'user_id': payment.user_id, 'payment_method': payment.payment_method, 'amount': payment.amount, 'status': payment.status} for payment in payments])
