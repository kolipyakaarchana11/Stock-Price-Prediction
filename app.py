import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(
    page_title="Stock Price Tracker",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #1a0b0f, #2b1118, #3b1721);
    color: #fff8f5;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

.hero {
    padding: 35px;
    border-radius: 24px;
    background: linear-gradient(135deg, #4a1625, #681f32, #7f2940);
    margin-bottom: 30px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.45);
    border: 1px solid #8f3a50;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 8px;
    color: #fff8f5;
}

.hero p {
    color: #e8c8cf;
    font-size: 17px;
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 15px;
    color: #f0c6a8;
}

.footer {
    text-align: center;
    color: #b98b96;
    margin-top: 40px;
    padding: 20px;
}

div[data-testid="stButton"] > button {
    width: 100%;
    border-radius: 12px;
    height: 48px;
    font-size: 17px;
    font-weight: 600;
    background: linear-gradient(90deg, #7a263d, #a33a52);
    color: white;
    border: 1px solid #b14a62;
    box-shadow: 0 5px 20px rgba(90,20,40,0.4);
}

div[data-testid="stButton"] > button:hover {
    background: linear-gradient(90deg, #8f2d47, #b8435d);
    color: white;
    border: 1px solid #d17a8d;
}

div[data-baseweb="select"] > div {
    background: #35151f;
    border: 1px solid #7f3a4c;
    border-radius: 12px;
    color: white;
}

div[data-baseweb="select"] span {
    color: #fff8f5;
}

.stCaption {
    color: #cda4ae;
}

div[data-testid="stDataFrame"] {
    border: 1px solid #6f2a3d;
    border-radius: 12px;
    overflow: hidden;
}

div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #35151f, #4a1b29);
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #703044;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <h1>📈 Stock Price Tracker</h1>
    <p>Select a stock and view its price history</p>
</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="section-title">🔎 Select a Stock</div>',
    unsafe_allow_html=True
)


stocks = {
    "Reliance Industries": "RELIANCE.NS",
    "Tata Consultancy Services": "TCS.NS",
    "Infosys": "INFY.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "ICICI Bank": "ICICIBANK.NS",
    "State Bank of India": "SBIN.NS",
    "ITC": "ITC.NS",
    "Tata Motors": "TATAMOTORS.NS",
    "Bharti Airtel": "BHARTIARTL.NS",
    "Wipro": "WIPRO.NS",
    "Larsen & Toubro": "LT.NS",
    "Adani Enterprises": "ADANIENT.NS",
    "Asian Paints": "ASIANPAINT.NS",
    "Hindustan Unilever": "HINDUNILVR.NS",
    "Maruti Suzuki": "MARUTI.NS",
    "Sun Pharma": "SUNPHARMA.NS",
    "Axis Bank": "AXISBANK.NS",
    "Bajaj Finance": "BAJFINANCE.NS",
    "Titan Company": "TITAN.NS",
    "Nestle India": "NESTLEIND.NS"
}


selected_stock = st.selectbox(
    "Choose a company",
    list(stocks.keys())
)


symbol = stocks[selected_stock]


st.caption(f"Stock Symbol: {symbol}")


if st.button("🚀 Get Stock Data"):

    with st.spinner("Fetching stock data..."):

        try:

            data = yf.download(
                symbol,
                period="1y",
                auto_adjust=True,
                progress=False
            )

            if data.empty:
                st.error("Unable to retrieve stock data.")
                st.stop()


            if isinstance(data.columns, pd.MultiIndex):

                data.columns = (
                    data.columns
                    .get_level_values(0)
                )


            for column in [
                "Open",
                "High",
                "Low",
                "Close",
                "Volume"
            ]:

                if column in data.columns:

                    if isinstance(
                        data[column],
                        pd.DataFrame
                    ):

                        data[column] = (
                            data[column]
                            .iloc[:, 0]
                        )


            data["MA5"] = (
                data["Close"]
                .rolling(5)
                .mean()
            )


            data["MA20"] = (
                data["Close"]
                .rolling(20)
                .mean()
            )


            data = data.dropna()


            st.markdown(
                '<div class="section-title">📈 Price History</div>',
                unsafe_allow_html=True
            )


            st.line_chart(
                data["Close"],
                height=450
            )


            st.markdown(
                '<div class="section-title">📊 Moving Averages</div>',
                unsafe_allow_html=True
            )


            chart_data = data[
                ["Close", "MA5", "MA20"]
            ]


            st.line_chart(
                chart_data,
                height=400
            )


            st.markdown(
                '<div class="section-title">📋 Recent Stock Data</div>',
                unsafe_allow_html=True
            )


            st.dataframe(
                data.tail(10),
                use_container_width=True
            )


            latest_price = float(
                data["Close"].iloc[-1]
            )

            previous_price = float(
                data["Close"].iloc[-2]
            )


            if latest_price > previous_price:

                st.markdown(
                    f"""
                    <div style="
                        background: linear-gradient(135deg, #7a263d, #9f3a55);
                        color: #ffffff;
                        font-size: 32px;
                        font-weight: 800;
                        text-align: center;
                        padding: 25px;
                        border-radius: 18px;
                        border: 2px solid #d6a76c;
                        margin-top: 25px;
                        box-shadow: 0 10px 30px rgba(0,0,0,0.35);
                    ">
                        📈 {selected_stock} IS UP
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            elif latest_price < previous_price:

                st.markdown(
                    f"""
                    <div style="
                        background: linear-gradient(135deg, #7a263d, #9f3a55);
                        color: #ffffff;
                        font-size: 32px;
                        font-weight: 800;
                        text-align: center;
                        padding: 25px;
                        border-radius: 18px;
                        border: 2px solid #d6a76c;
                        margin-top: 25px;
                        box-shadow: 0 10px 30px rgba(0,0,0,0.35);
                    ">
                        📉 {selected_stock} IS DOWN
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div style="
                        background: linear-gradient(135deg, #7a263d, #9f3a55);
                        color: #ffffff;
                        font-size: 32px;
                        font-weight: 800;
                        text-align: center;
                        padding: 25px;
                        border-radius: 18px;
                        border: 2px solid #d6a76c;
                        margin-top: 25px;
                        box-shadow: 0 10px 30px rgba(0,0,0,0.35);
                    ">
                        ➖ {selected_stock} HAS NO CHANGE
                    </div>
                    """,
                    unsafe_allow_html=True
                )


        except Exception as e:

            st.error(
                f"Unable to retrieve stock data: {e}"
            )


st.markdown(
    """
    <div class="footer">
        Stock Price Tracker
        <br>
        Data provided by Yahoo Finance
    </div>
    """,
    unsafe_allow_html=True
)