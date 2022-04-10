"""Plot the voter distribution from left to right."""
import matplotlib.pyplot as plt
import numpy as np

from src.data_utility.party_dictionary import PARTY_DICTIONARY
from src.data_utility.politbarometer.politbarometer import (
    calculate_voter_position,
    col_left_right,
    convert_left_right,
    load_voter_data,
    reduce_data,
)

# load party positions
party_positions = np.load("../data/saved/party_positions_pca.npy")

# plot party positions
fig, ax = plt.subplots()
ax.scatter(party_positions[:, 0], party_positions[:, 1], label="Parteien")
for party in range(6):
    ax.text(
        party_positions[party, 0],
        party_positions[party, 1],
        PARTY_DICTIONARY[party],
        ha="center",
    )
plt.xlabel("1. Hauptkomponente")
plt.ylabel("2. Hauptkomponente")

# load voter data
dataframe = load_voter_data()

# reduce data to Bundestagswahl 2017
dataframe = reduce_data(dataframe, year="2017", study=2391, month="August")

# calculate voter positions
dataframe = calculate_voter_position(party_positions, dataframe)

# convert and reduce using left-right
dataframe = convert_left_right(dataframe)

# plot voters in PC coordinates and colour left-right
scatter_voter = ax.scatter(
    dataframe["position_x"],
    dataframe["position_y"],
    s=1,
    c=dataframe[col_left_right],
    vmin=1,
    vmax=11,
    cmap="coolwarm",
    label="Wähler",
)
cbar = fig.colorbar(
    scatter_voter,
    ticks=[1, 6, 11],
)
cbar.ax.set_yticklabels(["0 sehr links", "5", "10 sehr rechts"])

plt.legend(loc="lower right")

# save plot
plt.savefig("../fig/voter_distribution_left_right.png")
