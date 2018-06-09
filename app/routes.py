from app import app
from urllib.request import urlopen, URLError, HTTPError
from io import BytesIO
from zipfile import ZipFile
from flask import jsonify
from http import HTTPStatus
from xml.etree import ElementTree
from app.models import gasStationModel, carburantModel


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
    return jsonify(stations=[station.jsonSerializer([carburant.jsonSerializer() for carburant in station.carburants])for station in stations])    

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
        gasStation = gasStationModel.gasStationModel(station.get('id'), station.get('latitude'), station.get('longitude'), station.get('cp'), station.get('pop'), station.get('ville'), station.get('adresse'))
        
        for price in station.findall('prix'):
            carburant = carburantModel.carburantModel(price.get('id'), price.get('nom'), price.get('valeur'),"stock", price.get('maj'))
            gasStation.carburants.append(carburant)

        for rupture in station.findall('rupture'):
            carburant = carburantModel.carburantModel(rupture.get('id'), rupture.get('nom'), "0","rupture", rupture.get('debut'))
            gasStation.carburants.append(carburant)
        
        gasStation.services.append([str(service.text, encoding='utf-8') for service in station.findall('service')]) 

        stations.append(gasStation)
    
    return stations