import streamlit as st  
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import yfinance as yf
from tradingview_ta import TA_Handler, Interval, Exchange
from pandas_datareader import data as pdr
import plotly.express as px
from plotly import graph_objects as go

st.set_page_config(layout="wide", page_title="Semi conductor companies share price")

st.title("Semi conductor share price companies")

stocks = ['NVDA','AVGO','GOOG','TSM','AAPL','QCOM','TXN']
selected_stock = st.selectbox('Select a company', stocks)


# import yfinance as yf
yf.pdr_override() # <== that's all it takes :-)

# download historical stock prices and cache the data.
@st.cache_data
def get_data(stock, start_date, end_date):
    data = yf.download(stock, start=start_date, end=end_date)
    return data


def get_info(stock):
    description = yf.Ticker(stock)
    description_info = description.info
    return description_info

data = get_data(selected_stock, "2024-03-01", "2024-04-01")
data_df = pd.DataFrame(data)
# st.dataframe(data) 
# st.write(get_info(selected_stock["longBusinessSummary"]))

st.title("selected_stock")
st.dataframe(data.head())


def plot_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data_df.index, y=data_df['Open'], name='Stock_open'))
    fig.add_trace(go.Scatter(x=data_df.index, y=data_df['Close'], name='Stock_close'))
    fig.update_layout(title='Stock Price scatter plots', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
    
plot_data()

# # st.dataframe(data) 
# st.write(get_info(data["longBusinessSummary"]))

