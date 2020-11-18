import os
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import loadData as ld


data = []
dataDirectory = './data'
pathToFiles = []
fileNames = os.listdir(dataDirectory)

for fileName in fileNames:
    pathToFiles.append(os.path.join(dataDirectory, fileName))


def formatDfSelectNames(index):
    return fileNames[index]


st.title("TP Vincent Maret Streamlit")

# We need a state manager in order to ask user to write an input without page refresh

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
data = ld.loadCsvDataFrames(pathToFiles, data)

# Select dataset
selectedDataframe = st.selectbox(
    "Choose dataset", range(len(fileNames)), format_func=formatDfSelectNames)

# Show dataset section
if len(data):
    dfRowsToDisplay = st.number_input(
        label='Number of rows from selected dataset to display', min_value=5)
    st.write(data[selectedDataframe].head(dfRowsToDisplay))

# display df columns
st.title('Dataset columns')
st.write(data[selectedDataframe].columns)

# display df types
st.title('Column types')
st.write(data[selectedDataframe].dtypes)

# display df shape
st.title('Dataset shape')
st.write(data[selectedDataframe].shape)

# display df stats
st.write('Dataset stats')
st.write(data[selectedDataframe].describe())

# heat map
st.title('Heatmap')
fig, ax = plt.subplots()
sns.heatmap(data[selectedDataframe].corr(), ax=ax, annot=True)
st.pyplot(fig)

# bar
st.title('Bar')
fig, ax = plt.subplots()
sns.countplot(data=data[selectedDataframe], ax=ax)
st.pyplot(fig)

# Custom visualisation
st.title('Custom visualisation')

graphs = ['heatmap', 'bar', 'box']

selectedGraph = st.selectbox(
    "Choose graph", graphs)

if selectedGraph in ['bar', 'box']:
    dfColumns = data[selectedDataframe].select_dtypes(
        include=['float64', 'int64']).columns.tolist()
    selectedCols = st.multiselect(
        "Choose graph", dfColumns)

shouldDisplayFig = False

fig, ax = plt.subplots()
if selectedGraph == 'heatmap':
    filteredData = data[selectedDataframe].corr()
    if len(filteredData):
        sns.heatmap(filteredData, ax=ax, annot=True)
        shouldDisplayFig = True

elif selectedGraph == 'bar' and len(selectedCols):
    sns.distplot(data[selectedDataframe][selectedCols[0]], ax=ax)
    shouldDisplayFig = True

elif selectedGraph == 'box' and len(selectedCols):
    plt.boxplot(data[selectedDataframe][selectedCols[0]])
    shouldDisplayFig = True

if shouldDisplayFig:
    st.pyplot(fig)
else:
    st.write('Fail to display graph. Retry with other inputs')
