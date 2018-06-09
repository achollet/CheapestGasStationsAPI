from app import db

class carburantDBPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gastation_id = db.Column(db.Integer, index=True, db.ForeignKey('gasStation.id'))
    carburant_id = db.Column(db.Integer, index=True, db.ForeignKey('carburant.id')
    value = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)