# Import necessary libraries
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime, timedelta

# Define the stocks and the time period
# For IDX stocks, we append ".JK" to the ticker
tickers = ['BBCA.JK', 'BREN.JK', 'PANI.JK']
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

# Download the stock data
# I use yf.download() which returns a pandas DataFrame
# The data is automatically indexed by date
try:
    data = yf.download(tickers, start=start_date, end=end_date)
    
    # I only need the 'Close' price for this analysis
    close_prices = data['Close']
    
    # Check if data was downloaded successfully
    if close_prices.empty:
        print("No data downloaded. Check ticker symbols and date range.")
    else:
        print("Stock data downloaded successfully:")
        print(close_prices.tail()) # Print the last 5 rows

        # Visualize the data
        sns.set_theme(style="whitegrid") # Set a nice theme for the plot
        plt.style.use("seaborn-v0_8-darkgrid") # Use a specific style for better aesthetics

        plt.figure(figsize=(14, 8)) # Create a figure with a specific size for better readability

        # Plot the closing price for each stock
        for stock in close_prices.columns:
            plt.plot(close_prices.index, close_prices[stock], label=stock)

        # Add titles and labels for clarity
        plt.title('Stock Price Performance (Last 365 Days)', fontsize=16)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Closing Price (IDR)', fontsize=12)
        plt.legend(title='Stock Ticker', fontsize=10)
        plt.xticks(rotation=45) # Rotate date labels for better fit
        plt.tight_layout() # Adjust plot to prevent labels from overlapping

        # Save the figure as an image file
        plt.savefig('stock_price_chart.png')
        print("\nChart has been saved as 'stock_price_chart.png'")

        # Display the plot
        plt.show()

except Exception as e:
    print(f"An error occurred: {e}")