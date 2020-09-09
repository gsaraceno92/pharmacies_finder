import os, sys
import tempfile
import unittest
import json
sys.path.append("../app")
from app import app
from base64 import b64encode


class BasicTestCase(unittest.TestCase):

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.client = app.test_client(self)

    def test_search_success(self):
        tester = self.client

        data = {
            "jsonrpc": "2.0",
            "method": "SearchNearestPharmacy",
            "params": {
                "currentLocation": {
                    "latitude": 41.10938993,
                    "longitude": 15.032101
                },
                "range": 1000,
                "limit": 1
            },
            "id": 1
        }
        response = tester.post('/api', data=json.dumps(data),headers=self.headers)
        
        self.assertEqual(response.status_code, 200)

    def test_validation_error(self):
        tester = self.client

        data = {
            "jsonrpc": "2.0",
            "method": "SearchNearestPharmacy",
            "params": {
                "currentLocation": {},
                "range": 1000,
                "limit": 1
            },
            "id": 1
        }
        response = tester.post('/api', data=json.dumps(data),headers=self.headers)
        
        self.assertEqual(response.status_code, 422)

    def test_type_error(self):
        tester = self.client

        data = {
            "jsonrpc": "2.0",
            "method": "SearchNearestPharmacy",
            "params": {
                "currentLocation": {},
                "range": 1000,
                "limit": "1"
            },
            "id": 1
        }
        response = tester.post('/api', data=json.dumps(data),headers=self.headers)
        
        self.assertEqual(response.status_code, 400)
    
if __name__ == '__main__':
    unittest.main()