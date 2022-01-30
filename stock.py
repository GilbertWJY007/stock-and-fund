import datetime
from typing import List
from price import Price
from datetime import date

class stock:
    def __init__(self, symbol: str, price_list: List[Price]):
        self.symbol = symbol
        self.price_list = price_list


    def get_return(prices: List[Price]):
        # （list里最后一天的收盘价-list第一天的开盘价）/list第一天的开盘价
        close_price = prices[len(prices)-1].close
        open_price = prices[1].open
        return (close_price - open_price)/open_price

    def get_daily_returns(prices: List[Price]):
        # parameter：价格list每一天的回报
        i = 1
        returns = []
        while i < len(prices):
            r = (prices[i].close - prices[i].open)/prices[i].open
            returns.append(r)
            i +=1
        return returns


    def get_beta(price_list: List[Price]):
        pass

    def get_period_prices(self,start_date: datetime.date, end_date: datetime.date):
        # 选定时间段里每一天的价格
        i = 1
        target_list = [Price]
        while i < len(self.price_list):
            a_day = datetime.timedelta(days = 1)
            if (self.price_list[i].date > (start_date - a_day) and self.price_list[i].date < (end_date + a_day)):
                target_list.append(self.price_list[i])
            i += 1
        return target_list
    
    def get_monthly_prices(self, month: int, year: int):
        #一个月中每一天的价格
        i = 1
        target_list = [Price]
        while i < len(self.price_list):
            if self.price_list[i].date.month == month and self.price_list[i].date.year == year:
                target_list.append(self.price_list[i])
            i += 1
        return target_list

    def get_annual_prices(self, year: int):
        # 一年中每一天的价格
        i = 1
        target_list = [Price]
        while i < len(self.price_list):
            if self.price_list[i].date.year == year:
                target_list.append(self.price_list[i])
            i += 1
        return target_list


