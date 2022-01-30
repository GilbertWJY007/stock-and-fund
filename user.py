import csv
from stock import stock
from price import Price
import datetime


def get_data(filename):
        csvFile = open(filename, "r")
        reader = csv.reader(csvFile)
        price_list = [Price]
        for info in reader:
            if reader.line_num == 1:
                continue
            newname = filename.replace(' ','-').split('.')
            symbol = newname[0]
            price_list.append(parse_price(symbol,info))
        csvFile.close()
        return price_list

def parse_price(symbol,curr_line):
        date = datetime.date.fromisoformat(curr_line[0])
        newPrice = Price(symbol,date,float(curr_line[1]),float(curr_line[5]),int(curr_line[6]))
        return newPrice

def run():
    #only for test
    price_list = get_data("TSLA.csv")
    stock_curr = stock("TSLA", price_list)
    date1 = date_generator('2021-01-05')
    date2 = date_generator('2021-01-06')
    lst = stock_curr.get_period_prices(date1,date2)
    print(stock.get_return(lst))
    i = 1
    while i < len(lst):
        print(lst[i].toString())
        i+=1

def date_generator(day: str):
        return datetime.date.fromisoformat(day)

if __name__ == '__main__':
    run()