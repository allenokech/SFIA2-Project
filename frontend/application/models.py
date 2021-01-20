from application import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.String(30), nullable=False)
    player_class = db.Column(db.String(30), nullable=False)
    build = db.Column(db.String(200), nullable=False)
