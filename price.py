import csv

class price:
    def __init__(self, symbol, date, open, close, volume):
        self.symbol = symbol
        self.open = open
        self.close = close #用adj close
        self.date = date
        self.volume = volume
        pass
    
    def get_data(filename):
        csvFile = open(filename, "r")
        reader = csv.reader(csvFile)
        daily_data = []
        for info in reader:
            if reader.line_num == 1:
                continue
            daily_data.append(info)
        csvFile.close()
        return daily_data

'''
['Date',       'Open',       'High',       'Low',        'Close',      'Adj Close',  'Volume'  ]
['2020-12-21', '666.239990', '668.500000', '646.070007', '649.859985', '649.859985', '58045300']
'''


    





