import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import loadData as ld

st.title("TP Vincent Maret Streamlit")
st.header("Simple Header")


userInput = st.text_input('Path to your data folder', './data/')

if userInput:
    if st.button("Load data"):
        csvPaths = ld.getCsvPaths(userInput)
        data = ld.loadCsvDataFrames(csvPaths)
        st.dataframe(data[0].head())
