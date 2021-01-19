from flask import Flask, render_template, request
import requests
from application import app, db

@app.route('/', methods=['GET', 'POST'])
def index():
    race_response = requests.get("http://service2:5001/race")
    player_class_response = requests.get("http://service3:5002/player_class")
    build_response = requests.post("http://service3:5003/player_class", json={"race" : race_response.text, "player_class" : player_class_response.text})
 
    return render_template('index.html', race=race_response.text, player_class=player_class_response.text, build=build_response.text)
