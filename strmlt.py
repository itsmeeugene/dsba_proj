import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def owner_num(x):
    if x == 'Test Drive Car':
        return 0
    if x == 'First Owner':
        return 1
    if x == 'Second Owner':
        return 2
    if x == 'Third Owner':
        return 3
    return 4


df = pd.read_csv("car.csv")

df['price_usd'] = df['selling_price'] / 83
df['owner_num'] = df['owner'].apply(owner_num)

st.markdown("The majority of cars are manual")
temp = pd.DataFrame({'count': df.transmission.value_counts(), 'transmission': df.transmission.value_counts().index})

fig1 = px.pie(temp, values='count', names='transmission')
st.plotly_chart(fig1)

st.markdown("The majority of cars listed are from around 2018")
fig2 = px.histogram(df, 'year')
st.plotly_chart(fig2)

st.markdown("The majority of cars listed are 5-seaters")

temp = pd.DataFrame({'count': df.seats.value_counts(), 'seats': df.seats.value_counts().index})
fig3 = px.bar(temp, x='seats', y='count')
st.plotly_chart(fig3)

st.markdown("The histogram of prices of manual diesel cars sold by dealers and inviduals doesn't provide any noticeable differene in price")

a = df[(df['transmission'] == 'Manual') & (df['fuel'] == 'Diesel') & (df['seller_type'] == 'Dealer')]['price_usd']
b = df[(df['transmission'] == 'Manual') & (df['fuel'] == 'Diesel') & (df['seller_type'] == 'Individual')]['price_usd']


temp = pd.DataFrame(dict(
    series=np.concatenate((["dealer"]*len(a), ["individual"]*len(b))),
    data=np.concatenate((a, b))
))

fig4 = px.histogram(temp, x="data", color="series", barmode="overlay")
st.plotly_chart(fig4)
