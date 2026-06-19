from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for Vendor Dash
inventory = {
    "101": {"name": "Wireless Mouse", "stock": 45, "price": 25.99},
    "102": {"name": "Mechanical Keyboard", "stock": 12, "price": 85.00}
}

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Vendor Dash API is live and running via Docker, version 2!"})

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

@app.route('/inventory/add', methods=['POST'])
def add_item():
    data = request.get_json()
    item_id = data.get('id')
    inventory[item_id] = {
        "name": data.get('name'),
        "stock": data.get('stock'),
        "price": data.get('price')
    }
    return jsonify({"message": "Item added to storefront", "item": inventory[item_id]}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)