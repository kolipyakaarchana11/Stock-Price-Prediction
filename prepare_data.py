import pandas as pd

data = pd.read_csv(
    "data/stock_data.csv",
    header=[0, 1],
    index_col=0
)

data.columns = data.columns.get_level_values(0)

data.index = pd.to_datetime(data.index)

print("Original Data:")
print(data.head())

print("\nMissing Values:")
print(data.isnull().sum())

data = data.dropna()

data["MA5"] = data["Close"].rolling(window=5).mean()
data["MA20"] = data["Close"].rolling(window=20).mean()

data["Return"] = data["Close"].pct_change()

data["Volatility"] = data["Return"].rolling(window=10).std()

data["Target"] = (
    data["Close"].shift(-1) > data["Close"]
).astype(int)

data = data.dropna()

data.to_csv("data/processed_data.csv")

print("\nProcessed Data:")
print(data.head())

print("\nData shape:")
print(data.shape)

print("\nProcessed data saved successfully.")