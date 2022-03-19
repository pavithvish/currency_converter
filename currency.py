import streamlit as st
from PIL import Image
import pandas as pd
import requests
import json



# Title



image = Image.open('logo.png')

st.image(image, width = 650)

st.title('Currency Converter App')
st.markdown("""
* Welcome to currency converter app. This app convert EURO currency to other currency.
* !! Euro Value is DEFAULT currency in this app!!

""")



st.sidebar.header('Input Options')

currency_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW','MYR', 'MXN', 'NOK', 'NZD',
 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY','USD', 'ZAR']
default_list = ['EUR']
base_price_unit = st.sidebar.selectbox(' Base currency for conversion', default_list)
symbols_price_unit = st.sidebar.selectbox('Select target currency to convert to', currency_list)



@st.cache
def load_data():
    url =''.join(['http://api.exchangeratesapi.io/v1/latest?access_key=19e9fde3f2e09e33a2d25bd5c4d6a1cc&format=1', base_price_unit, '&symbols=', symbols_price_unit])
    response = requests.get(url)
    data = response.json()
    base_currency = pd.Series( data['base'], name='base_currency')
    rates_df = pd.DataFrame.from_dict( data['rates'].items() )
    rates_df.columns = ['converted_currency', 'price']
    conversion_date = pd.Series( data['date'], name='date' )
    df = pd.concat( [base_currency, rates_df, conversion_date], axis=1 )
    return df

df = load_data()

st.header('Currency conversion')

st.write(df)
expander_bar = st.expander("About")
expander_bar.markdown("""
* REFERENCE : EUROPEAN CENTRAL BANK
""")
