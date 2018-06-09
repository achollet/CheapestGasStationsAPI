from app import db

class carburantDBModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(64)), index=True, unique=True)
    carburantPrices = db.relationship('carburantDBPrice', backref='carburant', lazy=True)

    def __repr__(self):
        return '<Carburant : {}>'.format(self.username)