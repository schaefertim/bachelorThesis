"""Try to load Wahl-O-Mat-2017.

data from https://github.com/gockelhahn/qual-o-mat-data
"""
import matplotlib.pyplot as plt

from src.data_utility.party_dictionary import PARTY_DICTIONARY
from src.data_utility.politbarometer.politbarometer import (
    calculate_voter_position,
    load_voter_data,
    reduce_data,
)
from src.data_utility.wahl_o_mat.wahl_o_mat import (
    load_opinion,
    load_statement,
    opinion_to_array,
    perform_pca,
    print_pca_significant_statements,
)

# load party data
dataframe_statement = load_statement()
party_positions = opinion_to_array(load_opinion(n_parties=6))

# compute pca and new party positions
party_positions, pca = perform_pca(party_positions)

# print most significant statements
print("pca explained variance ratio", pca.explained_variance_ratio_)
print_pca_significant_statements(pca, dataframe_statement)

# plot party positions
plt.scatter(party_positions[:, 0], party_positions[:, 1])
for party in range(6):
    plt.text(
        party_positions[party, 0],
        party_positions[party, 1],
        PARTY_DICTIONARY[party],
    )

# load voter data
dataframe = load_voter_data()

# reduce data to Bundestagswahl 2017
dataframe = reduce_data(dataframe, year="2017", study=2391, month="August")

# calculate voter positions
dataframe = calculate_voter_position(party_positions, dataframe)

# plot voters in PC coordinates
plt.scatter(dataframe["position_x"], dataframe["position_y"], s=1)

plt.savefig("../fig/voter_distribution.png")
