"""
This program will take market data and suggest an action (buy, sell. or hold)
"""
import yfinance as yf
    
# get stock data
def get_stock_data():
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")

    price = data["Close"]
    round_price = round(price,2).iloc[-1]
    print(f"${round_price}")
    
    
# Get ticker symbol
ticker = input("Enter a ticker symbol: ").strip().upper()

# calculate and give suggestion

get_stock_data()