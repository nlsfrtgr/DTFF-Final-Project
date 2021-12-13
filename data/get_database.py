# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 21:03:23 2021

@author: Antoine
"""



#pip install yfinance

import yfinance as yf
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
import os

def get_database (): 
    """
    

    Give the stock price of five stocks
    -------
    None.

    """

    list_tickers=['AAPL','INTC','F','PFE','T']
    tickers = yf.Tickers(list_tickers)

    end_data = date.today()

    start_data = date.today() - relativedelta(years=15)

    df = pd.DataFrame(tickers.download( start=start_data, end=end_data))
    
    data = df["Close"]
    
    input_direct = os.getcwd()
    output_direct = "/data/stock_prices.csv"
    res = input_direct+output_direct
    
    data.to_csv(res)
    
    return

get_database()