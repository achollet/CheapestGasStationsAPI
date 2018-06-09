from app import db

class gasStationTypeBDModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.String(25), index=True, unique=True, nullable=True)
    gasStations = db.relationship('gasStationDBModel', backref='gasStationType', lazy=True)