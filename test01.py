import unittest
import json
from flask import Flask
from api_01 import app, item_api

class TestItemAPI(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.items_data = [
            {"item": "Laptop", "price": 1200, "brand": "Dell"},
            {"item": "Smartphone", "price": 800, "brand": "Samsung"},
            {"item": "Headphones", "price": 100, "brand": "Sony"},
            {"item": "Keyboard", "price": 50, "brand": "Logitech"},
            {"item": "Mouse", "price": 30, "brand": "HP"},
        ]
        self.tearDown()

    def test_get_all_items(self):
        for item_data in self.items_data:
            item_api.add_item(item_data['item'])

        response = self.app.get('/items')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertIn('items', data)
        self.assertEqual(len(data['items']), len(self.items_data))
        self.tearDown()

    def test_get_single_item(self):
        for item_data in self.items_data:
            item_api.add_item(item_data['item'])

        expected_item = self.items_data[1]['item']
        response = self.app.get('/items/1')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('item', data)
        self.assertEqual(data['item'], expected_item)
        self.tearDown()

    def test_get_single_item_not_found(self):
        response = self.app.get('/items/10')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Item not found')
        self.tearDown()

    def test_add_item(self):
        item_data = {"item": "new_item"}
        response = self.app.post('/items', json=item_data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(item_api.get_items(), [item_data['item']])
        self.tearDown()

    def test_add_item_missing_data(self):
        response = self.app.post('/items', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Invalid data')
        self.tearDown()

    def test_update_item(self):
        for item_data in self.items_data:
            item_api.add_item(item_data['item'])

        index = 1
        new_item_data = {"new_item": "updated_item"}
        response = self.app.put(f'/items/{index}', json=new_item_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(item_api.get_item(index), new_item_data['new_item'])
        self.tearDown()

    def test_update_item_not_found(self):
        response = self.app.put('/items/10', json={"new_item": "updated_item"})
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Item not found')
        self.tearDown()

    def test_delete_item(self):
        for item_data in self.items_data:
            item_api.add_item(item_data['item'])

        item_to_delete = self.items_data[1]['item']
        response = self.app.delete('/items', json={'item': item_to_delete})

        self.assertEqual(response.status_code, 200)
        self.assertNotIn(item_to_delete, item_api.get_items())
        self.tearDown()

    def test_delete_item_not_found(self):
        response = self.app.delete('/items', json={'item': 'nonexistent_item'})
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Item not found')
        self.tearDown()

    def tearDown(self):
        item_api.items = []

if __name__ == '__main__':
    unittest.main()