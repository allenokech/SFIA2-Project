from flask import Flask, render_template, request, Response
import random
from application import app, db

@app.route('/race', methods=['GET'])
def race():
    race = ["Nord", "Imperial", "Breton", "Khajiit", "Dark Elf", "Wood Elf"]
    return Response(str(random.choice(race)), mimetype='text/plain')