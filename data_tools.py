import csv
import numpy as np
from sklearn.preprocessing import LabelEncoder


def load_data(filename, data_type):
    a = []
    with open(filename) as csv_file:
        data_file = csv.reader(csv_file)
        for row in data_file:
            a.append(row)

    arr = np.array(a)

    if data_type == 'train':
        X = arr[1:, 1:-1]
        y = arr[1:, -1]
        return X, y
    elif data_type == 'test':
        Y = arr[1:, 1:-1]
        return arr, Y


def merge_to_file(X, y):
    f = open('job_match.csv', 'w')
    try:
        writer = csv.writer(f)
        m = len(y)
        n = len(X[0])

        row = []
        for j in range(n):
            row.append(X[0, j])
        row.append('job match')
        writer.writerow(row)

        for i in range(m):
            row = []
            for j in range(n):
                row.append(X[i+1, j])
            row.append(y[i])
            writer.writerow(row)
    finally:
        f.close()


def convert_categorical(X):
    # Convert non-numeric data X array to numeric data and return the converted data
    le = LabelEncoder()
    n_features = len(X[0])
    X_new = le.fit_transform(X[:,0])
    for i in range (1, n_features):
        Xi = le.fit_transform(X[:,i])
        X_new = np.column_stack((X_new, Xi))
    return X_new