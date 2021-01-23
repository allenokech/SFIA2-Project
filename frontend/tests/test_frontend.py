from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app, db
from application.models import Character

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app
    
    def setUp(self):
        db.create_all()
        db.session.add(Character(race = "Argonian", player_class = "Entropist", build = "Mages who specialize in poison, decay, disease, and other damage over time spells as well as status ailments."))
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestGenerator(TestBase):
    def test_gen(self):
        response = self.client.get(url_for('gen'))
        self.assertEqual(response.status_code, 500)

class TestResponse(TestBase):
    def test_index(self):
        with requests_mock.mock() as g:
            g.get("http://character-gen_service2:5000/race", text = "Argonian")
            g.get("http://character-gen_service3:5000/player_class", text = "Entropist")
            g.post("http://character-gen_service4:5000/build", text = "Mages who specialize in poison, decay, disease, and other damage over time spells as well as status ailments.")
            
            response = self.client.get(url_for('gen'))
            self.assertNotIn(b"Redguard", response.data)
            self.assertIn(b"Entropist", response.data)
            self.assertIn(b"Mages who specialize in poison, decay, disease, and other damage over time spells as well as status ailments.", response.data)