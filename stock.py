import datetime
from typing import List
from price import price

class stock:
    def __init__(self, symbol: str, price_list: List[price]):
        self.symbol = symbol
        self.price_list = price_list


    def get_return(period):
        pass

    def get_beta(period):
        pass



    def get_period_prices(self,start_date: datetime.date, end_date: datetime.date):
        i = 0
        target_list = [price]
        while i < len(self.price_list):
            p = self.price_list[i]
            if (p.date > (start_date - datetime.timedelta(day = 1)) and p.date < (end_date + datetime.timedelta(day = 1))):
                target_list.append(p)
            i += 1
        return target_list
                
        # if start_date.isoweekday == 6 :
        #     new_start_date = start_date + datetime.timedelta(days=2)
        # if start_date.isoweekday == 7 :
        #     new_start_date = start_date + datetime.timedelta(days=1)
        # if end_date.isoweekday == 6:
        #     new_end_date = end_date - datetime.timedelta(days=1)
        # if end_date.isoweekday == 7:
        #     new_end_date = end_date - datetime.timedelta(days=2)
        # new_start_date = start_date
        # new_end_date = end_date

        


