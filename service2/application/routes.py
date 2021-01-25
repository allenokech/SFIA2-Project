from flask import Flask, render_template, request, Response
import random
from application import app

@app.route('/race', methods=['GET'])
def race():
    race = ["Redguard", "High Elf", "Argonian", "Orismer", "Dark Elf", "Wood Elf"]
    return Response(str(random.choice(race)), mimetype='text/plain')