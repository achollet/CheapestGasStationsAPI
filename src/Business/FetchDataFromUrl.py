from urllib.request import urlopen, URLError
from zipfile import ZipFile
from io import BytesIO

class FetchDataFromUrl:
    
    urls = {"now" : "https://donnees.roulez-eco.fr/opendata/instantane",
            "daily" : "https://donnees.roulez-eco.fr/opendata/jour",
            "year" : "https://donnees.roulez-eco.fr/opendata/annee"}
    
    def __init__(self):
        self.urls = {"now" : "https://donnees.roulez-eco.fr/opendata/instantane",
            "daily" : "https://donnees.roulez-eco.fr/opendata/jour",
            "year" : "https://donnees.roulez-eco.fr/opendata/annee"}

    def RetriveDataFromUrl(self, urlKey):
        url = self.urls[urlKey]
        try:
            response = urlopen(url)    
        except URLError as e:
            print(e.reason)

        zippedFile = BytesIO(response.read())
        unzippedFile = ZipFile(zippedFile)

        file = unzippedFile.Items

        return ""

         
