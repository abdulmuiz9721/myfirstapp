import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

data = pd.read_table('Data.csv', index_col = False,  sep = ',', skipinitialspace = True)
data

df = data.drop(['Substitution ','xG', 'xG Per Avg Match',
       'OnTarget',  'On Target Per Avg Match'], axis = 1)

df.head()

st.header("My First Streamlit App")

option = st.sidebar.selectbox(
    'Select',
     ['1','map','T n C'])


if option=='1':
    label = list(total_match_2019.index.values)
plt.pie(total_match_2019,labels=label,autopct='%1.1f%%')
plt.title("Total Played Match")
plt.show()

    st.line_chart(chart_data)

elif option=='map':
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
