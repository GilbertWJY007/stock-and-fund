from datetime import datetime

class Price:
    def __init__(self, symbol, date:datetime.date, open, close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open
        self.close = close #用adj close
        self.volume = volume 

    def toString(self):
        return "date: [{}], open: [{}], close: [{}], volume[{}]".format(self.date,self.open,self.close,self.volume)

    def get_date(self) -> datetime.date:
        return self.date
