import streamlit as st

import numpy as np
import pandas as pd

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
