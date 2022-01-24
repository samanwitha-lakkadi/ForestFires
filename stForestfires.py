
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

if st.checkbox('Show the raw data')
    data
