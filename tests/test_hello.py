import unittest
from hello import greet

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("World"), "Hello, World!")
