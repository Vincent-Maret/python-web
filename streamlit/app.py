import os
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataDirPath = './data'


def loadDataset(datasetPath):
    return pd.read_csv(datasetPath)


def getDataset(dirPath):
    fileNames = os.listdir(dirPath)
    selectedFile = st.selectbox("Choose dataset", fileNames)
    datasetPath = os.path.join(dirPath, selectedFile)
    return loadDataset(datasetPath)


st.title("TP Vincent Maret Streamlit")

data = getDataset(dataDirPath)

dfRowsToDisplay = st.number_input(
    label='Number of rows from selected dataset to display', min_value=5)
st.write(data.head(dfRowsToDisplay))

# display df columns
st.title('Dataset columns')
st.write(data.columns)

# display df types
st.title('Column types')
st.write(data.dtypes)

# display df shape
st.title('Dataset shape')
st.write(data.shape)

# display df stats
st.title('Dataset stats')
st.write(data.describe())

# heat map
st.title('Heatmap')
fig, ax = plt.subplots()
sns.heatmap(data.corr(), ax=ax, annot=True)
st.pyplot(fig)

# bar
st.title('Bar')
fig, ax = plt.subplots(figsize=(15, 3))
sns.countplot(data=data, ax=ax)
st.pyplot(fig)


# Custom visualisation
st.title('Custom visualisation')

graphs = ['heatmap', 'bar', 'box', 'lineplot']
numericDataOnly = data.select_dtypes(
    include=['float64', 'int64'])

selectedGraph = st.selectbox(
    "Choose graph", graphs)


if selectedGraph in ['bar', 'box', 'lineplot']:
    dfColumns = numericDataOnly.columns.tolist()

    if selectedGraph in ['bar', 'box']:
        selectedCols = st.selectbox(
            "Choose a field", dfColumns)
    else:
        selectedCols = st.multiselect(
            "Choose some fields", dfColumns)


shouldDisplayFig = False

fig, ax = plt.subplots()
if selectedGraph == 'heatmap':
    filteredData = data.corr()
    if len(filteredData):
        sns.heatmap(filteredData, ax=ax, annot=True)
        shouldDisplayFig = True

elif selectedGraph == 'bar' and selectedCols:
    sns.distplot(data[selectedCols], ax=ax)
    shouldDisplayFig = True

elif selectedGraph == 'box' and selectedCols:
    plt.boxplot(data[selectedCols])
    shouldDisplayFig = True

elif selectedGraph == 'lineplot' and len(selectedCols) == 2:
    sns.lineplot(x=selectedCols[0], y=selectedCols[1],
                 data=data, ax=ax)
    shouldDisplayFig = True

if shouldDisplayFig:
    st.pyplot(fig)
else:
    st.write('Fail to display graph. Retry with other inputs')
