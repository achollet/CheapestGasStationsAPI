from flask import jsonify

class gasStationModel:
    def __init__(self, id, latitude, longitude, zipcode, type, address, city):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.zipcode = zipcode
        self.type = type
        self.address = address
        self.city = city
        self.carburants = []
        self.services = []

    def jsonSerializer(self, carburantsJson):
        return {
            'id': self.id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'adresse': self.address,
            'ville': self.city,
            'zipcode': self.zipcode,
            'type' : self.type,
            'carburants': carburantsJson,
            'services': self.services
        }