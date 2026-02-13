"""
This program will take market data and suggest an action (buy, sell. or hold)
"""
import yfinance as yf
    
# get stock data
def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1mo")
    
        price = data["Close"]
        round_price = round(price,2).iloc[-1]
        moving_avg = round(price.rolling(10).mean().iloc[-1], 2)
        
        return round_price, moving_avg
    
    except:
        print("No data found")    

# calculate and give suggestion
def calculation(round_price, moving_avg):
    
    print(f"${round_price}")
    print(f"10-day average: ${moving_avg}")
    
    if round_price > moving_avg:
        print("Suggestion: Buy")
        
    elif round_price < moving_avg:
        print("Suggestion: Sell")
    
    else:
        print("Suggestion: Hold")
    
    
def main():
    # Get ticker symbol
    ticker = input("Enter a ticker symbol: ").strip().upper()
    round_price, moving_avg = get_stock_data(ticker)
    calculation(round_price, moving_avg)
if __name__ == "__main__":
    main()
