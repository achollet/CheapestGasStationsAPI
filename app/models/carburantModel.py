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