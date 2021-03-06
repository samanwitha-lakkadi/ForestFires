
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

# LOADING DATA
DATA_URL = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv"
)

"""
# Forest Fires

Abstract: This is a difficult regression task, where the aim is to predict the burned area of forest fires, in the northeast region of Portugal, by using meteorological and other data (https://archive.ics.uci.edu/ml/datasets/Forest+Fires)).


"""

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data = load_data(100000)


"## Summary"    
st.dataframe(data.describe())


"""
## Raw Data

We can see all the data here by pressing check button.
"""
#TODO: add code to show the raw data table only when the checkbox is selected 

if st.checkbox('Show the raw data'):
    data

"## Filtering Data by the Burned Area"
#TODO: add slider to the sidebar
min_area, max_area = st.sidebar.slider('area',value=[0,1100])


#TODO: using the min_area and max_area, store filtered data into data
data = data[data['area'].between(min_area,max_area)]


"The number of filtered data samples: ", data.shape[0]

   
fig, axes = plt.subplots(2,2)

# TODO: Using plot.scatter in pandas, plot X, Y in axes[0][0] (top-left subplot area)

axes[0][0].scatter(data['X'], data['Y'])
axes[0][0].set_xlabel('X')
axes[0][0].set_ylabel('Y')

# TODO: Using plot.hist in pandas, plot histogram of area data in axes[0][1] (top-right subplot area)
axes[0][1].hist(data['wind'],bins=5)
axes[0][1].set_xlabel('wind')
axes[0][1].set_ylabel('Frequency')

# TODO: Using plot in pandas, plot area for temp in axes[1][0] (bottom-left subplot area)
axes[1][0].scatter(data['temp'], data['area'])
axes[1][0].set_xlabel('temp')
axes[1][0].set_ylabel('area')

# TODO: Using plot in pandas, plot area for wind in axes[1][1] (bottom-right subplot area)
axes[1][1].scatter(data['wind'], data['area'])
axes[1][1].set_xlabel('wind')
axes[1][1].set_ylabel('area')

plt.tight_layout()
st.pyplot(fig)
