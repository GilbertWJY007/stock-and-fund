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

    def parse_price(curr_line):
        date = curr_line[0]
        open = curr_line[1]
        close = curr_line[5]
        volunm = curr_line[6]
        newPrice = price(date, open,)
        return newPrice



        return "price object"
'''
['Date',       'Open',       'High',       'Low',        'Close',      'Adj Close',  'Volume'  ]
['2020-12-21', '666.239990', '668.500000', '646.070007', '649.859985', '649.859985', '58045300']
'''


    





