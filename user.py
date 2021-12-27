import csv
from price import Price

price_list = []#后面能直接用 原处在line9

def get_data(filename):
        csvFile = open(filename, "r")
        reader = csv.reader(csvFile)
        #price_list = []
        for info in reader:
            if reader.line_num == 1:
                continue
            newname = filename.replace(' ','-').split('.')
            symbol = newname[0]
            price_list.append(Price.parse_price(symbol,info))
        csvFile.close()
        return price_list

def parse_price(symbol,curr_line):
        date = curr_line[0]
        newPrice = Price(symbol,date,float(curr_line[1]),float(curr_line[5]),int(curr_line[6]))
        return newPrice

def run():
    #only for test
    get_data("TSLA.csv")
    for p in price_list:
        if p.date == '2020-12-21':
            print("hit")
        else:
            print("false")
            break
    #

if __name__ == '__main__':
    run()