import numpy as np
import pandas as pd
# you may change the path of the dataset
data_input = pd.read_csv('diabetes_data_upload.csv', header=0)

data_processed = data_input.copy()
for i in data_input:
    for j in range(0, 520):
        if data_input[i][j] == "Yes":
            data_processed[i][j] = bool(1)
        if data_input[i][j] == "No":
            data_processed[i][j] = bool(0)
        if data_input[i][j] == "Positive":
            data_processed[i][j] = bool(1)
        if data_input[i][j] == "Negative":
            data_processed[i][j] = bool(0)
        if data_input[i][j] == "Male":
            data_processed[i][j] = bool(1)
        if data_input[i][j] == "Female":
            data_processed[i][j] = bool(0)

data_rules = data_processed.copy()
data_rules = data_rules.iloc[:, 1:]



