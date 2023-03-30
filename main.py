import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np

# FUNCTIONS
def getJsonData(url):
    res = requests.get(url)
    jsonData = ""
    if res.ok==True:
        jsonData = res.json()
        return jsonData
    else:
        st.error(res.reason)
        return nil

def debugExtractedList(jsondata, extracted, dataframe):
    st.subheader("debug info")
    st.json(jsondata[0])
    st.text(jsondata[0].get("id"))
    st.json(extracted)
    # https://docs.streamlit.io/library/api-reference/data/st.dataframe
    st.dataframe(dataframe)
    st.subheader("end debug info")


# ENTRY POINT
st.title("Cen Project")
st.header("Crypto App")
st.subheader("Json from api")

deserializedJson = getJsonData("https://api.coinpaprika.com/v1/tickers")


if deserializedJson != nil:
    # list comprehension
    #https://stackoverflow.com/questions/45655721/how-to-create-a-list-from-json-keyvalues-in-python3
    # NOTE this is slow but do i care
    extracted = [
                    [coinObj['id'] for coinObj in deserializedJson],
                    [
                        [coinObj['beta_value'] for coinObj in deserializedJson],
                        [coinObj['circulating_supply'] for coinObj in deserializedJson]
                    ]
                ]

    #https://www.geeksforgeeks.org/python-transpose-elements-of-two-dimensional-list/
    extracted[1] = np.transpose(extracted[1])

    #https://docs.streamlit.io/library/api-reference/charts/st.bar_chart
    #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
    windowOffset = st.slider("view diffent coins", min_value=0, max_value=100, step=1)
    windowSize   = st.slider("how many coins to view at once", min_value=4, max_value=20, step=1)
    coinLabels = extracted[0][windowOffset:windowOffset+windowSize]
    coinData   = extracted[1][windowOffset:windowOffset+windowSize]
    chartDataFrame = pd.DataFrame(coinData, coinLabels, columns = ["beta values", "supply pct"])
    st.bar_chart(chartDataFrame)
    
    # Just to see what is going on
    debugExtractedList(deserializedJson, extracted, chartDataFrame)



