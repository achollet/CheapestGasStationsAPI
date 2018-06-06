from app import app
from urllib.request import urlopen, URLError, HTTPError
from io import BytesIO
from zipfile import ZipFile
from flask import jsonify
from http import HTTPStatus

@app.route('/')
def index():
    try :
        reponse = urlopen("https://donnees.roulez-eco.fr/opendata/jour")
    except HTTPError as e:
        print(e.code)
    except URLError as e:
    
    unzippedfile = ZipFile(BytesIO(reponse.read()))
    file = unzippedfile.filelist[0].filename

    if file is None or file == "":
        return HTTPStatus.NOT_FOUND

    xmlString = ""

    for line in unzippedfile.open(file).readlines():
        xmlString += line.decode(encoding="utf-8", errors="ignore")

    return jsonify(xmlString)
