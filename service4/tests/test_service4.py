from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestBuild(TestBase):
    def test_archer(self):
        response = self.client.post(url_for('build'), data = "Archer",)
        self.assertIn(b'Peerless marksman who relies almost entirely on bows or cross bows to get the job done.', response.data)