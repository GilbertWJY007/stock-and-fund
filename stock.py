import datetime
from typing import List
from price import price

class stock:
    def __init__(self, symbol: str, price_list: List[price]):
        self.symbol = symbol
        self.price_list = price_list


    def get_return(price_list: List[price]):
        
        pass

        

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

        


