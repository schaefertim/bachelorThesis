"""Try to load Wahl-O-Mat-2017.

data from https://github.com/gockelhahn/qual-o-mat-data
"""
import matplotlib.pyplot as plt
import numpy as np

from src.data_utility.party_dictionary import (
    PARTY_DICTIONARY,
    PARTY_MAPPING_WAHL_O_MAT_2017,
)
from src.data_utility.wahl_o_mat.wahl_o_mat import (
    load_opinion,
    load_statement,
    opinion_to_array,
    perform_pca,
    print_pca_significant_statements,
)

# load data
dataframe_statement = load_statement()
party_positions = opinion_to_array(load_opinion(n_parties=6))

# compute pca and new party positions
party_positions, pca = perform_pca(party_positions)

# permute party index such that they are in usual order
party_positions_temp = np.zeros_like(party_positions)
for i in range(6):
    party_positions_temp[PARTY_MAPPING_WAHL_O_MAT_2017[i]] = party_positions[i]
party_positions = party_positions_temp

# save most significant statements to file
print("pca explained variance ratio", pca.explained_variance_ratio_)
print_pca_significant_statements(pca, dataframe_statement, filepath="../fig")

# plot party positions
plt.scatter(party_positions[:, 0], party_positions[:, 1])
for party in range(6):
    plt.text(
        party_positions[party, 0],
        party_positions[party, 1],
        PARTY_DICTIONARY[party],
    )

# save plot and calculated data
plt.savefig("../fig/party_positions.png")
np.save("../data/saved/party_positions_pca", party_positions)
