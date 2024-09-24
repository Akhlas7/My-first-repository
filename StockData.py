import yfinance as yf
from orca.orca import start

ticker = input("Enter the ticket: ")
from_data = input("Enter the start date (YYYY-MM-DD): ")
to_date = input("Enter the end date (YYY-MM-DD): ")


stock_data = yf.download(ticker,start=from_data, end=to_date)
stock_data.to_csv("stock_data.csv")
print("stock data written to stock_data.csv")

