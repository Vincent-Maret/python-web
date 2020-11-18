import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import loadData as ld


data = []
datasetNames = ['Chess', 'UFO']
pathToFiles = ['./data/chess.csv', './data/ufo.csv']


def formatDfSelectNames(opt):
    return datasetNames[opt]


st.title("TP Vincent Maret Streamlit")

# Load datasets section

# try to implement a state !!!!!!!
# pathToFiles = st.text_input(
#     'Path to your data directory or csv file', './data/')

# if pathToFiles:
#     if st.button("Load data"):
#         # try to implement a state
#         # csvPaths = ld.getCsvPaths(pathToFiles)
#         res = ld.loadCsvDataFrames(pathToFiles, data, datasetNames)
#         data = res[0]
#         # datasetNames = res[1]

# Load data
data = ld.loadCsvDataFrames(pathToFiles, data, datasetNames)[0]

# Select dataset
selectedDataframe = st.selectbox(
    "Choose dataset", range(len(datasetNames)), format_func=formatDfSelectNames)

# Show dataset section
if len(data):
    dfRowsToDisplay = st.number_input(
        label='Number of rows from selected dataset to display', min_value=5)
    st.write(data[selectedDataframe].head(dfRowsToDisplay))

# display df columns
st.write('Dataset columns')
st.write(data[selectedDataframe].columns)

# display df types
st.write('Column types')
st.write(data[selectedDataframe].dtypes)

# display df shape
st.write('Dataset shape')
st.write(data[selectedDataframe].shape)
