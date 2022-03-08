"""Try to load Wahl-O-Mat-2017.

data from https://github.com/gockelhahn/qual-o-mat-data
"""

import json
import pandas as pd
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
party_positions_pca_0 = party_positions.dot(pca.components_[0])
party_positions_pca_1 = party_positions.dot(pca.components_[1])

plt.scatter(party_positions_pca_0, party_positions_pca_1)
for party in parties:
    plt.text(
        party_positions_pca_0[party],
        party_positions_pca_1[party],
        file_party[party]['name'],
    )

filepath = "../data/ZA2391_v13-0-0.sav"
col_study = "v1"
col_participant = "v2"
col_month = "v3"
col_year = "v4"
col_party = "v6"
col_party_last = "v7"
col_spd = "v8"
col_cdu = "v9"
col_left_right = "v22"
usecols = [col_study, col_participant, col_month, col_year, col_party, col_party_last, col_spd, col_cdu, col_left_right]
# usecols = [f"v{i}" for i in range(1, 10)]
dataframe = pd.read_spss(filepath, usecols=usecols)

dataframe = dataframe[dataframe[col_year] == "2017"]
dataframe = dataframe[dataframe[col_study] == 2391]
dataframe = dataframe[dataframe[col_month] == "August"]

dataframe = dataframe[dataframe[col_party] == "SPD"]
dataframe = dataframe[dataframe[col_spd] != "KA"]
dataframe = dataframe[dataframe[col_cdu] != "KA"]

"""position_voter_spd_0 = (
                               party_positions_pca_0[1] * np.exp(dataframe[col_spd]) +
                               party_positions_pca_0[0] * np.exp(dataframe[col_cdu])
                       ) / (np.exp(dataframe[col_spd]) + np.exp(dataframe[col_cdu]))"""

print(type(dataframe[col_spd]))
plt.show()
