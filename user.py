from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    preferences = db.Column(db.String(200))

    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
