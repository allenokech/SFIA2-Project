from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestGenerator(TestBase):
    def test_gen(self):
        response = self.client.get(url_for('gen'))
        self.assertEqual(response.status_code, 500)