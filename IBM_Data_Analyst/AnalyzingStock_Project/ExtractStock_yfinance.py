!pip install yfinance==0.1.67
!pip install pandas==1.3.3

import yfinance as yf
import pandas as pd

# Using 'Ticker' module to create an object that allow access to data extraction
apple = yf.Ticker("AAPL")

#Extract stock information using attribute 'info'
apple_info=apple.info
apple_info
apple_info['country'] # Get Country of the stock
apple_info['sector'] # Get Sector of the stock

#Extracting share price in DataFrame format
apple_share_price_data = apple.history(period="max")
apple_share_price_data.head()  #See the top 5 rows of the share price DataFrame
apple_share_price_data.reset_index(inplace=True) # Reset the index of the DataFrame
apple_share_price_data.plot(x="Date", y="Open") #Plot the open price against date

#Extract Dividends
apple.dividends
apple.dividends.plot()
