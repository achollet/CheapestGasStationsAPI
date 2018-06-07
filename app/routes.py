from app import app
from urllib.request import urlopen, URLError, HTTPError
from io import BytesIO
from zipfile import ZipFile
from flask import jsonify
from http import HTTPStatus
from xml.etree import ElementTree

@app.route('/', methods=['GET'])
def index():
    try :
        reponse = urlopen("https://donnees.roulez-eco.fr/opendata/jour")
    except HTTPError as e:
        print(e.code)
    except URLError as e:
        print(e.args)
    
    xmlString = FileUnzipper(reponse)

    if xmlString is None or xmlString == "":
        return HTTPStatus.NOT_FOUND

    stations = XmlUnserializer(xmlString)
    var = carburantDBModel()

    return jsonify(stations=[station.jsonSerializer() for station in stations])    

def FileUnzipper(file):
    unzippedfile = ZipFile(BytesIO(file.read()))
    file = unzippedfile.filelist[0].filename

    if file is None or file == "":
        return file

    xmlString = ""

    for line in unzippedfile.open(file).readlines():
        xmlString += line.decode(encoding="utf-8", errors="ignore")

    return xmlString


def XmlUnserializer(xmlString):
    root = ElementTree.fromstring(xmlString)
    stations = []
    
    for station in root.findall('pdv'):
        gasStationModel(station.get('id'), station.get('latitude'), station.get('longitude'), station.get('cp'), station.get('pop'))
        gasStationModel.adresse = station.get('adresse')
        gasStationModel.ville = station.get('ville')

        for price in station.findall('prix'):
            carburantModel(price.get('id'), price.get('nom'), price.get('valeur'),"stock", price.get('maj'))
            gasStationModel.carburants.append(carburantModel)

        for rupture in station.findall('rupture'):
            carburantModel(rupture.get('id'), rupture.get('nom'), "0","rupture", rupture.get('debut'))
            gasStationModel.carburants.append(carburantModel)

        for service in station.findall('service'):
            gasStationModel.services.append(str(service.text, encoding='utf-8')) 

        stations.append(gasStationModel)
    
    return stations        
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

    def jsonSerializer(self):
        return {
            'id': self.id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'adresse': self.adresse,
            'ville': self.ville,
            'zipcode': self.zipcode,
            'type' : self.type,
            'carburants': [carburant.jsonSerializer() for carburant in self.carburants],
            'services': self.services
        }

class carburantModel:
    def __init__(self, id, name, price, status, updateDate):
        self.id = id
        self.name = name
        self.price = price
        self.status = status
        self.updateDate = updateDate

    def jsonSerializer(self):
        return {
            'id': self.id,
            'label': self.name,
            'price': self.price,
            'status': self.status,
            'lastUpdate' : self.updateDate
        }