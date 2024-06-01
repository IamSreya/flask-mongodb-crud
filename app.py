from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb+srv://<username>:<password>@atlascluster.yctusyg.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")
db = client.get_database('<dbname>')
collection = db['<collection_name>']

@app.route('/add', methods=['POST'])
def add_item():
    data = request.get_json()
    result = collection.insert_one(data)
    return jsonify({"_id": str(result.inserted_id)}), 201

@app.route('/items', methods=['GET'])
def get_items():
    items = list(collection.find())
    for item in items:
        item['_id'] = str(item['_id'])
    return jsonify(items), 200

@app.route('/item/<id>', methods=['GET'])
def get_item(id):
    item = collection.find_one({"_id": ObjectId(id)})
    if item:
        item['_id'] = str(item['_id'])
        return jsonify(item), 200
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route('/update/<id>', methods=['PUT'])
def update_item(id):
    data = request.get_json()
    result = collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.matched_count > 0:
        return jsonify({"msg": "Item updated"}), 200
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route('/delete/<id>', methods=['DELETE'])
def delete_item(id):
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count > 0:
        return jsonify({"msg": "Item deleted"}), 200
    else:
        return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
