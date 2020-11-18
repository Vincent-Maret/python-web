import os
import pandas as pd


def getCsvPaths(path):
    assert os.path.exists(
        path), "Directory not found: "+str(path)

    csvPaths = []
    for (root, dirNames, fileNames) in os.walk(path):
        for fileName in fileNames:
            if fileName.endswith('.csv'):
                csvPaths.append(os.path.join(root, fileName))
        break

    return csvPaths


def loadCsvDataFrames(paths):
    assert len(paths) > 0, 'No CSV file found in givent directory.'

    data = []
    for path in paths:
        data.append(pd.read_csv(path))
    return data
