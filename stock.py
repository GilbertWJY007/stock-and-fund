import datetime
from typing import List
from price import price
from datetime import date

class stock:
    def __init__(self, symbol: str, price_list: List[price]):
        self.symbol = symbol
        self.price_list = price_list


    def get_return(prices: List[price]):
        close_price = prices[len(prices)-1].close
        open_price = prices[1].open
        return (close_price - open_price)/open_price

    def get_daily_returns(prices: List[price]):
        i = 1
        returns = []
        while i < len(prices):
            r = (prices[i].close - prices[i].open)/prices[i].open
            returns.append(r)
            i +=1
        return returns


    def get_beta(price_list: List[price]):
        pass



    def get_period_prices(self,start_date: datetime.date, end_date: datetime.date):
        i = 1
        target_list = [price]
        while i < len(self.price_list):
            a_day = datetime.timedelta(days = 1)
            if (self.price_list[i].date > (start_date - a_day) and self.price_list[i].date < (end_date + a_day)):
                target_list.append(self.price_list[i])
            i += 1
        return target_list
    
    def get_monthly_prices(self, month: int, year: int):
        i = 1
        target_list = [price]
        while i < len(self.price_list):
            if self.price_list[i].date.month == month and self.price_list[i].date.year == year:
                target_list.append(self.price_list[i])
            i += 1
        return target_list

    def get_annual_prices(self, year: int):
        i = 1
        target_list = [price]
        while i < len(self.price_list):
            if self.price_list[i].date.year == year:
                target_list.append(self.price_list[i])
            i += 1
        return target_list


