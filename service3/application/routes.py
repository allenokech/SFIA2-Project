from flask import Flask, render_template, request, Response
import random
from application import app

@app.route('/player_class', methods=['GET'])
def player_class():
    player_class = ["Duelist", "Spellsword", "Warlock", "Rogue", "Entropist", "Battlemage", "Blacksmith", "Knight"]
    return Response(str(random.choice(player_class)), mimetype='text/plain')