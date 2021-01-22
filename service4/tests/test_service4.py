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
    
    def test_dual(self):
        response = self.client.post(url_for('build'), data = "Dual-Wield",)
        self.assertIn(b'Aggressive fighters who wield weapons in both hands.', response.data)
    
    def test_illusionist(self):
        response = self.client.post(url_for('build'), data = "Illusionist",)
        self.assertIn(b'Mages who specialize in manipulating minds, altering perceptions of friend and foe alike.', response.data)
    
    def test_assassin(self):
        response = self.client.post(url_for('build'), data = "Assassin",)
        self.assertIn(b'Quiet killers, these types attack from the shadows against unsuspecting prey.', response.data)
    
    def test_alchemist(self):
        response = self.client.post(url_for('build'), data = "Alchemist",)
        self.assertIn(b'Characters skilled in the crafting and use of powerful potions and deadly poisons.', response.data)
    
    def test_nightblade(self):
        response = self.client.post(url_for('build'), data = "Nightblade",)
        self.assertIn(b'Mages who work from the shadows, using stealth to supplement their magical abilities.', response.data)
    
    def test_barbarian(self):
        response = self.client.post(url_for('build'), data = "Barbarian",)
        self.assertIn(b'Brutish, aggressive fighters who prefer an overwhelming offense over a cautious defense.', response.data)
    
    def test_juggernaut(self):
        response = self.client.post(url_for('build'), data = "Juggernaut",)
        self.assertIn(b'Tough, resiliant characters covered head to toe in nigh impenetrable heavy armor.', response.data)
    
    def test_else(self):
        response = self.client.post(url_for('build'), data = "Build Not Compatible",)
        self.assertNotIn(b'Aggressive fighters who wield weapons in both hands.', response.data)