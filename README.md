# 📈 Stock Price Prediction Using Machine Learning

## 📌 Project Overview

Stock Price Prediction is a Python-based Machine Learning project designed to analyze historical stock market data and identify stock price trends.

The project combines **Machine Learning, Data Analysis, Data Visualization, and Streamlit** to provide an interactive platform where users can select a stock and view its historical performance, moving averages, recent prices, and market trends.

The application retrieves stock market information using **Yahoo Finance** and presents the results through an easy-to-use Streamlit web interface.

---

## 🎯 Objectives

The main objectives of this project are:

- To collect historical stock market data.
- To preprocess and clean stock price data.
- To calculate technical indicators such as moving averages.
- To analyze stock price trends.
- To apply Machine Learning techniques for stock movement prediction.
- To visualize stock market data.
- To create an interactive web application using Streamlit.
- To provide users with an easy way to explore stock information.

---

## ✨ Key Features

### 📊 Stock Data Collection

The project uses the `yfinance` library to retrieve historical stock market data from Yahoo Finance.

### 📈 Stock Price Visualization

Users can view stock price movements through graphical representations.

### 📉 Moving Averages

The application calculates:

- **MA5** – 5-day moving average
- **MA20** – 20-day moving average

Moving averages help identify general stock price trends.

### 🤖 Machine Learning

The project uses a Machine Learning model to analyze stock-related features and predict stock movement.

### 🌐 Interactive Streamlit Application

The Streamlit interface allows users to select stocks and view their information without needing to interact with Python code directly.

### 🏦 Multiple Indian Stocks

The application provides information for several popular Indian companies.

---

## 🧰 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| Streamlit | Web application |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| Joblib | Model saving/loading |
| yFinance | Stock market data |
| Matplotlib | Data visualization |

---

## 📂 Project Structure

```text
Stock-Price-Prediction/
│
├── app.py
├── data_collection.py
├── prepare_data.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── stock_data.csv
│   └── processed_data.csv
│
└── model/
    └── stock_model.pkl
