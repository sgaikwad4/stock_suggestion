"""
This program will take market data and suggest an action (buy, sell. or hold)
"""
# Import yfinance library 
import yfinance as yf
    
# get stock data
def get_stock_data(ticker):
    try:
        # set stock to the ticker (user input)
        stock = yf.Ticker(ticker)
        # get one month history of stock
        data = stock.history(period="1mo")
    
        price = data["Close"]
        # Round the price to two decimal places
        round_price = round(price,2).iloc[-1]
        # get the average prices from thr last ten days
        moving_avg = round(price.rolling(10).mean().iloc[-1], 2)
        return round_price, moving_avg
    
    except Exception as e :
        # If there's an error than return none and state the error
        print(f"Error: {e}")
        return None, None

# calculate and give suggestion
def calculation(round_price, moving_avg):
    # print the ten day average and current price
    print(f"10-day average: ${moving_avg}")
    print(f"${round_price}")
    # if current price is over ten day average then suggest to buy
    if round_price > moving_avg:
        print("Suggestion: Buy")
    # if current price is less than ten day average then suggest to sell
    elif round_price < moving_avg:
        print("Suggestion: Sell")
    # if current price is the same as the ten day average then suggest to hold
    else:
        print("Suggestion: Hold")
    
    
def main():
    while True:
        # Get ticker symbol
        ticker = input("Enter a ticker symbol: ").strip().upper()
        # Call get_stock_data function
        round_price, moving_avg = get_stock_data(ticker)
        # if returned data is none then print no data found
        if round_price is None:
            print("No data found for that ticker")
        # if data isn't none then call calculation function
        else:    
            calculation(round_price, moving_avg)
            break
        
if __name__ == "__main__":
    main()