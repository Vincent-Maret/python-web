import os
import pandas as pd


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
