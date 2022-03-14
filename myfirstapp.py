import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go



df=pd.read_csv("Number of Cases of Covid-19 in 2020.csv")

df.head()

st.dataframe(df)

st.sidebar.checkbox("State", True, key=1)
select = st.sidebar.selectbox('Select a State',df['State'])


#get the state selected in the selectbox
state_data = df[df['State'] == select]
select_year = st.sidebar.radio("Level", ('Level 1','Level 2','Total'))

def get_total_dataframe(dataset):
    total_dataframe = pd.DataFrame({
    'Level':['Level 1','Level 2','Total'],
    'Number of Covid Case':(dataset.iloc[0]['Level 1'],dataset.iloc[0]['Level 2'],dataset.iloc[0]['Total'])})
    return total_dataframe

    'State' =['Johor', 'Kedah','Kelantan', 'Melaka','Negeri Sembilan', 'Pahang', 'Pulau Pinang','Perak', 'Perlis']

    Total = [814, 292, 407, 632, 1167, 474, 167, 628, 61]

#The plot
fig = go.Figure(
    go.Pie(
    labels = 'State',
    values = Total,
    hoverinfo = "label+percent",
    textinfo = "value"
))
    
st.header("Pie chart")
st.plotly_chart(fig)


