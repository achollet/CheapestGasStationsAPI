from flask import jsonify

class gasStationModel:
    def __init__(self, id, latitude, longitude, zipcode, type):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.zipcode = zipcode
        self.type = type
        self.adresse = ""
        self.ville = ""
        self.carburants = []
        self.services = []

    def jsonSerializer(self, carburantsJson):
        return {
            'id': self.id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'adresse': self.adresse,
            'ville': self.ville,
            'zipcode': self.zipcode,
            'type' : self.type,
            'carburants': carburantsJson,
            'services': self.services
        }