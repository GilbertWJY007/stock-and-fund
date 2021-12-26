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
        price_list = []
        for info in reader:
            if reader.line_num == 1:
                continue
            price_list.append(price.parse_price(info))
        csvFile.close()
        return price_list

    def parse_price(filename,curr_line):
        symbol = filename
        date = float(curr_line[0])
        newPrice = price(symbol,date,float(curr_line[1]),float(curr_line[5]),int(curr_line[6]))
        return newPrice




'''
['Date',       'Open',       'High',       'Low',        'Close',      'Adj Close',  'Volume'  ]
['2020-12-21', '666.239990', '668.500000', '646.070007', '649.859985', '649.859985', '58045300']
'''



    





