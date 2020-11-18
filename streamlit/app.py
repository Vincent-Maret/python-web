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

# display df stats
st.write('Dataset stats')
st.write(data[selectedDataframe].describe())

# heat map
st.write('Heatmap')
fig, ax = plt.subplots()
sns.heatmap(data[selectedDataframe].corr(), ax=ax, annot=True)
st.pyplot(fig)

# bar
st.write('Bar')
fig, ax = plt.subplots()
sns.countplot(data=data[selectedDataframe], ax=ax)
st.pyplot(fig)

# Custom visualisation
st.write('Custom visualisation')

graphs = ['heatmap', 'bar']

selectedGraph = st.selectbox(
    "Choose graph", graphs)

if selectedGraph == 'bar':
    dfColumns = data[selectedDataframe].select_dtypes(
        include=['float64', 'int64']).columns.tolist()
    selectedCols = st.multiselect(
        "Choose graph", dfColumns)


fig, ax = plt.subplots()
if selectedGraph == 'heatmap':
    sns.heatmap(data[selectedDataframe].corr(), ax=ax, annot=True)

elif selectedGraph == 'bar' and len(selectedCols):
    sns.distplot(data[selectedDataframe][selectedCols[0]], ax=ax)

st.pyplot(fig)
