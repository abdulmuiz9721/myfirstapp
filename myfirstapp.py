import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt



st.header("My First Streamlit App")


option = st.sidebar.selectbox(
    'Select',
     ['Players with most goals in 2019','2','T n C'])

#select data

def load_data(nrows):
    data = pd.read_table('Data.csv', index_col = False,  sep = ',', skipinitialspace = True)
    df = data.drop(['Substitution ','xG', 'xG Per Avg Match',
       'OnTarget', 'On Target Per Avg Match'], axis = 1)
    df =data[(data["Year"] > 2018) & (data["Year"] < 2020)]
    df2 = df[df['League'].isin(['Premier League', 'La Liga', 'Serie A', 'Bundesliga'])]
    df3 = df2[df2["Goals"] > 15]
    return df3









if option=='Players with most goals in 2019':
  
  

    chart_data = px.bar(df3, 
        x='Player Names',
        y='Goals',
        
        st.bar_chart(chart_data['2019_data'])


    

elif option=='2':
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(map_data)

else:

    st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
    show = st.checkbox('I agree the terms and conditions')
    if show:
        st.write(pd.DataFrame({
        'Intplan': ['yes', 'yes', 'yes', 'no'],
        'Churn Status': [0, 0, 0, 1]
        }))
