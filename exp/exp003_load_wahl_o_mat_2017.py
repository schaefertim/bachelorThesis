"""Try to load Wahl-O-Mat-2017.

data from https://github.com/gockelhahn/qual-o-mat-data
"""

import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

filepath_opinion = "../data/wahl_o_mat_2017/opinion.json"
with open(filepath_opinion) as fp:
    file = json.load(fp)
filepath_statement = "../data/wahl_o_mat_2017/statement.json"
with open(filepath_statement) as fp:
    file_statement = json.load(fp)
    no_statements = len(file_statement)
filepath_party = "../data/wahl_o_mat_2017/party.json"
with open(filepath_party) as fp:
    file_party = json.load(fp)

parties = list(range(6))
party_positions = np.zeros([len(parties), no_statements])
for item in file:
    if item['party'] in parties:
        party_positions[item['party'], item['statement']] = item['answer']
# replace 2 with 0.5 due to this being the neutral position
party_positions = np.where(party_positions == 2, 0.5, party_positions)

pca = PCA(n_components=2).fit(party_positions)
print("pca explained variance ratio", pca.explained_variance_ratio_)
pca_argsort = np.argsort(np.abs(pca.components_), axis=1)[:, ::-1]
print("statements from first PCA")
for statement in pca_argsort[0, :5]:
    print(
        statement,
        file_statement[statement]['label'],
        ": ",
        file_statement[statement]['text'],
        pca.components_[0, statement],
    )

print("\nstatements from second PCA")
for statement in pca_argsort[1, :5]:
    print(
        statement,
        file_statement[statement]['label'],
        ": ",
        file_statement[statement]['text'],
        pca.components_[1, statement],
    )

plt.scatter(
    party_positions.dot(pca.components_[0]),
    party_positions.dot(pca.components_[1]),
    )
for party in parties:
    plt.text(
        party_positions.dot(pca.components_[0])[party],
        party_positions.dot(pca.components_[1])[party],
        file_party[party]['name'],
    )
plt.show()
