from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    category = db.Column(db.String(50))
    sustainability = db.Column(db.Integer)

    def __init__(self, name, category, sustainability):
        self.name = name
        self.category = category
        self.sustainability = sustainability
