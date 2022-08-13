import streamlit as st
import requests
import pandas as pd
import numpy as np

'''
# TaxiFareModel front
'''


'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:

'''
pickup_date = st.date_input('Insert pickup date')
pickup_time = st.time_input('Insert pickup time')
pickup_datetime = f'{pickup_date} {pickup_time}'
##a= pd.to_datetime(date_time
pickup_longitude=st.number_input('Insert pickup longitude')
pickup_latitude=st.number_input('Insert pickup latitude')
dropoff_longitude=st.number_input('Insert dropoff longitude')
dropoff_latitude=st.number_input('Insert dropoff latitude')
passenger_count= st.selectbox('Select number of passengers', list(range(1, 9)))



'''

## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''


params={
        "pickup_datetime":pickup_datetime,
        "pickup_longitude":pickup_longitude,
        "pickup_latitude":pickup_latitude,
        "dropoff_longitude":dropoff_longitude,
        "dropoff_latitude":dropoff_latitude,
        "passenger_count":passenger_count
        }
st.text(params)

response = requests.request("GET", url, params=params)

st.text(response.json())
