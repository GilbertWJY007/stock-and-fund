import yfinance as yf
#import pandas as pd
#import numpy as np

spy_ohlc_df = yf.download('MFST', start='2021-07-25', end='2022-01-25')
print(spy_ohlc_df)

