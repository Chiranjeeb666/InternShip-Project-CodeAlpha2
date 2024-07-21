import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

class StockPortfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, start_date, end_date):
        stock_data = self.fetch_stock_data(symbol, start_date, end_date)
        self.stocks[symbol] = stock_data

    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]

    def fetch_stock_data(self, symbol, start_date, end_date):
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        return stock_data

    def calculate_portfolio_metrics(self):
        for symbol, stock_data in self.stocks.items():
            stock_data['Daily Return'] = stock_data['Adj Close'].pct_change()

    def plot_stock_trends(self):
        for symbol, stock_data in self.stocks.items():
            plt.figure(figsize=(10, 6))
            sns.lineplot(data=stock_data['Adj Close'])
            plt.title(f"{symbol} Stock Price Trend")
            plt.xlabel('Date')
            plt.ylabel('Adjusted Close Price')
            plt.show()

    def display_portfolio(self):
        for symbol, stock_data in self.stocks.items():
            print(f"Stock: {symbol}")
            print(stock_data.head())
            print()

def main():
    portfolio = StockPortfolio()

    while True:
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Plot Stock Trends")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            portfolio.add_stock(symbol, start_date, end_date)
        elif choice == "2":
            symbol = input("Enter stock symbol: ")
            portfolio.remove_stock(symbol)
        elif choice == "3":
            portfolio.display_portfolio()
        elif choice == "4":
            portfolio.calculate_portfolio_metrics()
            portfolio.plot_stock_trends()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()