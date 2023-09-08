from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

PANTRY_ID = "your-pantry-id"

# Endpoint to add a key-value pair to the Pantry
@app.route('/add-item', methods=['POST'])
def add_item():
    data = request.json
    basket_key = data.get('basket_key')
    value = data.get('value')
    
    if not basket_key or not value:
        return jsonify({"error": "Both basket_key and value are required"}), 400
    
    pantry_url = f"https://getpantry.cloud/apiv1/pantry/{PANTRY_ID}/basket/{basket_key}"
    response = requests.post(pantry_url, json={"value": value})
    
    if response.status_code == 200:
        return jsonify({"message": "Item added successfully"}), 201
    else:
        return jsonify({"error": "Failed to add item"}), 500

# Endpoint to retrieve the value associated with a specified basket key
@app.route('/get-item', methods=['GET'])
def get_item():
    basket_key = request.args.get('basket_key')
    
    if not basket_key:
        return jsonify({"error": "basket_key is required"}), 400
    
    pantry_url = f"https://getpantry.cloud/apiv1/pantry/{PANTRY_ID}/basket/{basket_key}"
    response = requests.get(pantry_url)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify({"value": data.get('value')}), 200
    else:
        return jsonify({"error": "Item not found"}), 404

# Endpoint to list all baskets under a specified Pantry
@app.route('/list-baskets', methods=['GET'])
def list_baskets():
    pantry_url = f"https://getpantry.cloud/apiv1/pantry/{PANTRY_ID}"
    response = requests.get(pantry_url)
    
    if response.status_code == 200:
        data = response.json()
        baskets = data.get('baskets', [])
        return jsonify({"baskets": baskets}), 200
    else:
        return jsonify({"error": "Failed to list baskets"}), 500

# Endpoint to update the value associated with a specified basket key
@app.route('/update-item', methods=['PUT'])
def update_item():
    data = request.json
    basket_key = data.get('basket_key')
    new_value = data.get('value')
    
    if not basket_key or not new_value:
        return jsonify({"error": "Both basket_key and new value are required"}), 400
    
    pantry_url = f"https://getpantry.cloud/apiv1/pantry/{PANTRY_ID}/basket/{basket_key}"
    response = requests.put(pantry_url, json={"value": new_value})
    
    if response.status_code == 200:
        return jsonify({"message": "Item updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to update item"}), 500

# Endpoint to delete a specific basket
@app.route('/delete-item', methods=['DELETE'])
def delete_item():
    basket_key = request.args.get('basket_key')
    
    if not basket_key:
        return jsonify({"error": "basket_key is required"}), 400
    
    pantry_url = f"https://getpantry.cloud/apiv1/pantry/{PANTRY_ID}/basket/{basket_key}"
    response = requests.delete(pantry_url)
    
    if response.status_code == 200:
        return jsonify({"message": "Item deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to delete item"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=9443)
