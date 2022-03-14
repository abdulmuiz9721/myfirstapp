import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

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

state_total = get_total_dataframe(state_data)

if st.sidebar.checkbox("Graph", True, key=2):
    st.markdown("## **Bar Graph**")
    st.markdown("### Total number of cases "  % (select))
    if not st.checkbox('Hide Graph', False, key=1):
        state_total_graph = px.bar(
        state_total, 
        x='State',
        y='Total',
        labels={'Total':'Total %s' % (select)},
        color='State')
        st.plotly_chart(state_total_graph)


