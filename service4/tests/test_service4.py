from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestBuild(TestBase):
    def test_archer(self):
        response = self.client.post(url_for('build'), data = "Duelist",)
        self.assertIn(b'Agile fighters who prefer finesse over brute strength.', response.data)
    
    def test_dual(self):
        response = self.client.post(url_for('build'), data = "Spellsword",)
        self.assertIn(b'Powerful melee combatants who augment their fighting skills with various spells.', response.data)
    
    def test_illusionist(self):
        response = self.client.post(url_for('build'), data = "Warlock",)
        self.assertIn(b'Those who harness magical power through unconventional means such as, but not limited to blood magic or pacts with higher beings.', response.data)
    
    def test_assassin(self):
        response = self.client.post(url_for('build'), data = "Rogue",)
        self.assertIn(b'Scoundrels willing to employ dirty, underhanded, and often illicit tactics to get their way.', response.data)
    
    def test_alchemist(self):
        response = self.client.post(url_for('build'), data = "Entropist",)
        self.assertIn(b'Mages who specialize in poison, decay, disease, and other damage over time spells as well as status ailments.', response.data)
    
    def test_nightblade(self):
        response = self.client.post(url_for('build'), data = "Battlemage",)
        self.assertIn(b'Mages who thrive in the heat of battle, preferring deadly close range spells.', response.data)
    
    def test_barbarian(self):
        response = self.client.post(url_for('build'), data = "Blacksmith",)
        self.assertIn(b'Characters immensely skilled in the art of creating and tempering steel.', response.data)
    
    def test_juggernaut(self):
        response = self.client.post(url_for('build'), data = "Knight",)
        self.assertIn(b'Honorable defenders willing to take the brunt of any attack in place of their allies.', response.data)
    
    def test_else(self):
        response = self.client.post(url_for('build'), data = "Build Not Compatible",)
        self.assertNotIn(b'Aggressive fighters who wield weapons in both hands.', response.data)