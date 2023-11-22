
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

plt.style.use('fivethirtyeight')

from fredapi import Fred

fred_key = 'c8fbc9ea000e097e9c17f242cc43c517'

fred = Fred(api_key=fred_key)

sp_search = fred.search('S&P')
sp_search

sp500 = fred.get_series(series_id='SP500')
sp500

sp500.plot(figsize=(10, 5), title='S&P 500')

unrate = fred.get_series(series_id='UNRATE')
unrate.plot(figsize=(10, 5), title='Unemployment Rate')