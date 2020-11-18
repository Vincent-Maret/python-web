import os
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("TP Vincent Maret Streamlit")
st.header("Simple Header")


def getCsvPaths(path):
    assert os.path.exists(
        path), "File not found at path: "+str(path)

    csvPaths = []
    for (root, dirNames, fileNames) in os.walk(path):
        for fileName in fileNames:
            if fileName.endswith('.csv'):
                csvPaths.append(os.path.join(root, fileName))

    return csvPaths


def loadCsvDataFrames(paths):
    data = []
    for path in paths:
        data.append(pd.read_csv(path))
    return data


userInput = st.text_input('Path to your data folder', './data/')
st.write(userInput)

if userInput:
    if st.button("Load data"):
        csvPaths = getCsvPaths(userInput)
        data = loadCsvDataFrames(csvPaths)
        data[0].head()
