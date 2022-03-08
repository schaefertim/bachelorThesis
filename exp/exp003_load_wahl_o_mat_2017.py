"""Try to load Wahl-O-Mat-2017.

data from https://github.com/gockelhahn/qual-o-mat-data
"""

import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

from src.data_utility.party_dictionary import PARTY_DICTIONARY
from src.data_utility.wahl_o_mat.wahl_o_mat import opinion_to_array, load_opinion, load_statement

dataframe_statement = load_statement()
party_positions = opinion_to_array(load_opinion(n_parties=6))

pca = PCA(n_components=2).fit(party_positions)
print("pca explained variance ratio", pca.explained_variance_ratio_)
pca_argsort = np.argsort(np.abs(pca.components_), axis=1)[:, ::-1]
print("statements from first PCA")
for statement in pca_argsort[0, :5]:
    print(
        statement,
        dataframe_statement.iloc[statement]['label'],
        ": ",
        dataframe_statement.iloc[statement]['text'],
        pca.components_[0, statement],
    )

print("\nstatements from second PCA")
for statement in pca_argsort[1, :5]:
    print(
        statement,
        dataframe_statement.iloc[statement]['label'],
        ": ",
        dataframe_statement.iloc[statement]['text'],
        pca.components_[1, statement],
    )

plt.scatter(
    party_positions.dot(pca.components_[0]),
    party_positions.dot(pca.components_[1]),
    )
for party in range(6):
    plt.text(
        party_positions.dot(pca.components_[0])[party],
        party_positions.dot(pca.components_[1])[party],
        PARTY_DICTIONARY[party],
    )
plt.show()
