# from flask import Flask, jsonify, request

# class ItemAPI:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item):
#         self.items.append(item)

#     def get_items(self):
#         return self.items

#     def get_item(self, index):
#         if 0 <= index < len(self.items):
#             return self.items[index]
#         else:
#             return None  # Return None for non-existing items

#     def update_item(self, index, new_item):
#         if 0 <= index < len(self.items):
#             self.items[index] = new_item
#         else:
#             raise IndexError("Index out of range")

#     def delete_item(self, item):
#         if item in self.items:
#             self.items.remove(item)
#         else:
#             raise ValueError("Item not found")

# app = Flask(__name__)
# item_api = ItemAPI()

# @app.route('/items', methods=['GET'])
# def get_all_items():
#     items = item_api.get_items()
#     return jsonify({'items': items})

# @app.route('/items/<int:index>', methods=['GET'])
# def get_single_item(index):
#     item = item_api.get_item(index)
#     if item is not None:
#         return jsonify({'item': item})
#     else:
#         return jsonify({'error': 'Item not found'}), 404

# @app.route('/items', methods=['POST'])
# def add_item():
#     data = request.get_json()
#     if 'item' in data:
#         item_api.add_item(data['item'])
#         return jsonify({'message': 'Item added successfully'}), 201
#     else:
#         return jsonify({'error': 'Invalid data'}), 400

# @app.route('/items/<int:index>', methods=['PUT'])
# def update_item(index):
#     data = request.get_json()
#     new_item = data.get('new_item')
#     try:
#         item_api.update_item(index, new_item)
#         return jsonify({'message': 'Item updated successfully'})
#     except IndexError:
#         return jsonify({'error': 'Item not found'}), 404

# @app.route('/items', methods=['DELETE'])
# def delete_item():
#     data = request.get_json()
#     item = data.get('item')
#     try:
#         item_api.delete_item(item)
#         return jsonify({'message': 'Item deleted successfully'})
#     except ValueError:
#         return jsonify({'error': 'Item not found'}), 404

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify, request

class ItemAPI:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

    def get_item(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        else:
            return None  # Return None for non-existing items

    def update_item(self, index, new_item):
        if 0 <= index < len(self.items):
            self.items[index] = new_item
        else:
            raise IndexError("Index out of range")

    def delete_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            raise ValueError("Item not found")

app = Flask(__name__)
item_api = ItemAPI()

@app.route('/items', methods=['GET'])
def get_all_items():
    items = item_api.get_items()
    print(f"GET request to /items. Items: {items}")
    return jsonify({'items': items})

@app.route('/items/<int:index>', methods=['GET'])
def get_single_item(index):
    item = item_api.get_item(index)
    if item is not None:
        print(f"GET request to /items/{index}. Item: {item}")
        return jsonify({'item': item})
    else:
        print(f"GET request to /items/{index}. Item not found")
        return jsonify({'error': 'Item not found'}), 404

@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    if 'item' in data:
        item_api.add_item(data['item'])
        print(f"POST request to /items. Added item: {data['item']}")
        return jsonify({'message': 'Item added successfully'}), 201
    else:
        print("POST request to /items. Invalid data.")
        return jsonify({'error': 'Invalid data'}), 400

@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    data = request.get_json()
    new_item = data.get('new_item')
    try:
        item_api.update_item(index, new_item)
        print(f"PUT request to /items/{index}. Item updated successfully.")
        return jsonify({'message': 'Item updated successfully'})
    except IndexError:
        print(f"PUT request to /items/{index}. Item not found.")
        return jsonify({'error': 'Item not found'}), 404

@app.route('/items', methods=['DELETE'])
def delete_item():
    data = request.get_json()
    item = data.get('item')
    try:
        item_api.delete_item(item)
        print(f"DELETE request to /items. Item deleted successfully: {item}")
        return jsonify({'message': 'Item deleted successfully'})
    except ValueError:
        print(f"DELETE request to /items. Item not found: {item}")
        return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    print("Starting the server...")
    app.run(debug=True)
