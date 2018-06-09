from app import db

class gasStationDBModel(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    latitude = db.Column(db.Float, index=True, nullable=False)
    longitude = db.Column(db.Float, index=True, nullable=False)
    zipcode = db.Column(db.String(6), nullable=False)
    city = db.Column(db.String(50), nullable=False )
    address = db.Colum(db.String(150, nullable=False)
    type_id = db.Column(db.Integer, index=True, db.ForeignKey('gasStationType.id'))
    carburants = db.relationship('carburantDBPrice', backref='gasStation', lazy=True)
    services = db.Column(db.String(50))
 