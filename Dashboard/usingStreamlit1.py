import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
#Simple stock price app
Shown are the stock closing price and volume of google!

""")
#https://towardDatascience.com/how to get-stock-data-using python-c0de1df17e75
#define the ticker symbol
tickerSymbol='GooGL'
#get data on this ticker
tickerData=yf.Ticker(tickerSymbol)
#get the historical pricefor this ticker
tickerDf=tickerData.history(period='1d',start='2010-5-31',end='2020-5-31')
#open high low close volume dividende stock splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


