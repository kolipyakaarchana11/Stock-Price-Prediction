import yfinance as yf

symbol = "RELIANCE.NS"

data = yf.download(
    symbol,
    start="2015-01-01",
    end="2026-01-01",
    auto_adjust=True
)

print(data.head())
print(data.tail())

data.to_csv("data/stock_data.csv")

print("Stock data saved successfully.")