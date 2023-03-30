import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np

# KEY: eB8BYJO4uFGlHVXb
# docs
# https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getproducts
# Need to create an account. Cannot use api without authenfification
url = "https://api.coinbase.com/api/v3/brokerage/products"
header = {"X-CB-ACCESS-KEY": "eB8BYJO4uFGlHVXb", "Content-Type" : "application/json"}



res = requests.get(url, headers = header)
st.error(res)

data = ""

if res.ok==True:
    data = res.json()
else:
    st.error(res.reason)

st.title("Miguel's Webapp")
st.header("Crypto App")
st.subheader("Json from api")

if data != "":
    st.json(data)




