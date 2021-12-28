import csv
from typing import List
from stock import stock
from price import price
import datetime


def get_data(filename):
        csvFile = open(filename, "r")
        reader = csv.reader(csvFile)
        price_list = [price]
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
        newPrice = price(symbol,date,float(curr_line[1]),float(curr_line[5]),int(curr_line[6]))
        return newPrice

def run():
    #only for test
    price_list = get_data("TSLA.csv")
    stock_curr = stock("TSLA", price_list)
    print(price_list[1].date)
    i = 0 
    while i < len(price_list):
        temp = price(price_list[i].symbol,price_list[i])
        print(price_list[i].get_date())
        i += 1
    # date1 = date_generator('2021-01-02')
    # date2 = date_generator('2021-02-02')
    # print(stock_curr.get_period_prices(date1, date2))
    
def date_generator(day: str):
        return datetime.date.fromisoformat(day)

if __name__ == '__main__':
    run()





