from datetime import datetime
from app import db


class GasStation(db.Model):
    __tablename__ = 'GasStations'
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, index=True, nullable=False)
    longitude = db.Column(db.Float, index=True, nullable=False)
    address = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    zipCode = db.Column(db.String(5), nullable=False)
    type = db.Column(db.String(1), nullable=False)
    open = db.Column(db.String(5), nullable=False)
    close = db.Column(db.String(5), nullable=False)
    closingDays = db.Column(db.String(20), nullable=True)
    services = db.Column(db.String(150), nullable=True)
    carburantData = db.relationship(
        'GasStationCarburantData', backref='GasStations', lazy='dynamic')


class Carburant(db.Model):
    __tablename__ = 'Carburants'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(50), index=True, nullable=False, unique=True)
    carburantData = db.relationship(
        'GasStationCarburantData', backref='Carburants', lazy='dynamic')


class Service(db.Model):
    __tablename__ = 'Services'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(50), index=True, nullable=False, unique=True)


class GasStationCarburantData(db.Model):
    __tablename__ = 'GasStationCarburantData'
    id = db.Column(db.Integer, primary_key=True)
    gasStationId = db.Column(db.Integer, db.ForeignKey(
        'GasStations.id'), index=True)
    carburantId = db.Column(db.Integer, db.ForeignKey(
        'Carburants.id'), index=True)
    price = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, nullable=False, default=True)
    lastUpdate = db.Column(db.DateTime, index=True, nullable=False)
