from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app
from application.models import Character

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app
    
    def setUp(self):
        db.create_all()
        db.session.add(Character(race = "Dark Elf", player_class = "Assassin", build = "Quiet killers, these types attack from the shadows against unsuspecting prey."))
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
            g.get("http://character-gen_service2:5000/race", text = "Dark Elf")
            g.get("http://character-gen_service3:5000/player_class", text = "Assassin")
            g.post("http://character-gen_service2:5000/build", text = "Quiet killers, these types attack from the shadows against unsuspecting prey.")
            
            response = self.client.get(url_for('gen'))
            self.assertIn(b"Nord", response.data)
            self.assertNotIn(b"Assassin", response.data)
            self.assertNotIn(b"Quiet killers, these types attack from the shadows against unsuspecting prey.", response.data)