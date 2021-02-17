from anomaly import *
import yaml
import json
with open("input.yaml") as f:
    document = yaml.safe_load(f)
    hyperparameters = document['hyperparameters']
    contamination = hyperparameters['contamination']
    n_neighbors = hyperparameters['n_neighbors']
    length = hyperparameters['length']

with open("realAdExchange/labels.json") as f:
    labels = json.load(f)

# append labels from the json file to datasets
def create_labeled_df(filename, labels):
    df = pd.read_csv(filename)
    df['outlier'] = 0
    outliers = labels[filename]
    for outlier in outliers:
        df.loc[df['timestamp'] == outlier,'outlier'] = 1
    return df

cpcs = []
for i in range(2,5):
    filename = "realAdExchange/exchange-" + str(i) + "_cpc_results.csv"
    df = create_labeled_df(filename, labels)
    cpcs.append(df)

cpms = []
for i in range(2,5):
    filename = "realAdExchange/exchange-" + str(i) + "_cpm_results.csv"
    df = create_labeled_df(filename, labels)
    cpms.append(df)

for i in range(3):
    print("Anomalies for cpc_" + str(i+2))
    predicted = knn_by_part(cpcs[i], contamination, n_neighbors, length)
    get_anomalies(cpcs[i], predicted)

for i in range(3):
    print("Anomalies for cpm_" + str(i+2))
    predicted = knn_by_part(cpms[i], contamination, n_neighbors, length)
    get_anomalies(cpms[i], predicted)
