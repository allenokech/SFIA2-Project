from flask import Flask, render_template, request, Response
import random
from application import app

@app.route('/build', methods=['POST'])
def build():
    data_sent = request.data.decode('utf-8')
    if player_class == "Archer":
        build = 'Peerless marksman who relies almost entirely on bows or cross bows to get the job done.'
    elif player_class == "Dual-Wield":
        build == 'Aggressive fighters who wield weapons in both hands.'
    elif player_class == "Illusionist":
        build == 'Mages who specialize in manipulating minds, altering perceptions of friend and foe alike.'
    elif player_class == "Assassin":
        build == 'Quiet killers, these types attack from the shadows against unsuspecting prey.'
    elif player_class == "Alchemist":
        build == 'Characters skilled in the crafting and use of powerful potions and deadly poisons.'
    elif player_class == "Nightblade":
        build == 'Mages who work from the shadows, using stealth to supplement their magical abilities.'
    elif player_class == "Barbarian":
        build == 'Brutish, aggressive fighters who prefer an overwhelming offense over a cautious defense.'
    elif player_class == "Juggernaut":
        build == 'Tough, resiliant characters covered head to toe in nigh impenetrable heavy armor.'
    
    return Response(build, mimetype='text/plain')