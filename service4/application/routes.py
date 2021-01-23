from flask import Flask, render_template, request, Response
import random
from application import app

@app.route('/build', methods=['POST'])
def build():
    player_class = request.data.decode('utf-8')

    if player_class == "Duelist":
        build = 'Agile fighters who prefer finesse over brute strength.'
    elif player_class == "Spellsword":
        build = 'Powerful melee combatants who augment their fighting skills with various spells.'
    elif player_class == "Warlock":
        build = 'Those who harness magical power through unconventional means such as, but not limited to blood magic or pacts with higher beings.'
    elif player_class == "Rogue":
        build = 'Scoundrels willing to employ dirty, underhanded, and often illicit tactics to get their way.'
    elif player_class == "Entropist":
        build = 'Mages who specialize in poison, decay, disease, and other damage over time spells as well as status ailments.'
    elif player_class == "Battlemage":
        build = 'Mages who thrive in the heat of battle, preferring deadly close range spells.'
    elif player_class == "Blacksmith":
        build = 'Characters immensely skilled in the art of creating and tempering steel.'
    elif player_class == "Knight":
        build = 'Honorable defenders willing to take the brunt of any attack in place of their allies.'
    
    else:
        build = "Build not compatible"

    return Response(build, mimetype='text/plain')