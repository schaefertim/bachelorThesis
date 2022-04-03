"""Try to load Wahl-O-Mat-2017.

data from https://github.com/gockelhahn/qual-o-mat-data
"""
import matplotlib.pyplot as plt
import numpy as np

from src.data_utility.party_dictionary import PARTY_DICTIONARY
from src.data_utility.politbarometer.politbarometer import (
    calculate_voter_position,
    load_voter_data,
    reduce_data,
)

# load party positions
party_positions = np.load("../data/saved/party_positions_pca.npy")

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
np.save(
    "../data/saved/voter_positions",
    dataframe[["position_x", "position_y"]].to_numpy(),
)
