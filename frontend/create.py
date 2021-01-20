from application import db
from application.models import Character

db.drop_all()
db.create_all()