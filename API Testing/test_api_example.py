import unittest
import requests

class TestSampleAPI(unittest.TestCase):
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def test_get_posts(self):
        response = requests.get(f"{self.BASE_URL}/posts")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_post(self):
        payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        response = requests.post(f"{self.BASE_URL}/posts", json=payload)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data["title"], payload["title"])
        self.assertEqual(data["body"], payload["body"])
        self.assertEqual(data["userId"], payload["userId"])

if __name__ == "__main__":
    unittest.main()