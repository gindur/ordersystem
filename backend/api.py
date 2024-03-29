from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import utils.csv_handler as data

csv_path = "data/orders.csv"
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

@app.route('/api/orders', methods=['GET'])
def get_orders():
    orders = data.process_orders(csv_path)
    return jsonify(orders)

@app.route('/api/customers', methods=['GET'])
def get_customers():
    _,customers, _  = data.process_orders(csv_path)
    return jsonify(customers)

if __name__ == '__main__':
    app.run(debug=True, port=5000)