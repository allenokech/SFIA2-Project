from flask import Flask, render_template, request, jsonify
import requests
from application.models import Character
from application import app, db

@app.route('/', methods=['GET', 'POST'])
def gen():
    race_response = requests.get("http://character-gen_service2:5000/race")
    player_class_response = requests.get("http://character-gen_service3:5000/player_class")
    build_response = requests.post("http://character-gen_service4:5000/build", data = player_class_response.text)
    
    new_build = Character(race = race_response.text, player_class = player_class_response.text, build = build_response.text)
    db.session.add(new_build)
    db.session.commit()

    previous = Character.query.first()
    
    return render_template('index.html', race=race_response.text, player_class=player_class_response.text, build=build_response.text, previous=previous)
