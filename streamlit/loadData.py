import os
import pandas as pd
import streamlit as st
import time

################################
# No use anymore, I need a state manager in order to keep data after page refresh
################################


def getCsvPaths(path):
    assert os.path.exists(
        path), "File or directory not found: "+str(path)

    if os.path.isfile(path) and path.endswith('.csv'):
        return [path]

    else:
        csvPaths = []
        for (root, dirNames, fileNames) in os.walk(path):
            for fileName in fileNames:
                if fileName.endswith('.csv'):
                    csvPaths.append(os.path.join(root, fileName))
            break

        return csvPaths


@st.cache
def loadCsvDataFrames(paths, data):
    assert len(paths) > 0, 'No CSV file found in given directory.'

    for path in paths:
        data.append(pd.read_csv(path))
    return data
