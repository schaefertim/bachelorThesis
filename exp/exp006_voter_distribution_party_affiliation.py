"""Plot the party affiliation of voters."""
import matplotlib.pyplot as plt
import numpy as np

from src.data_utility.party_dictionary import PARTY_DICTIONARY
from src.data_utility.politbarometer.politbarometer import (
    calculate_voter_position,
    col_party,
    convert_party_affiliation,
    load_voter_data,
    reduce_data,
)

# load party positions
party_positions = np.load("../data/saved/party_positions_pca.npy")

# plot party positions
fig, ax = plt.subplots()
ax.scatter(party_positions[:, 0], party_positions[:, 1])
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

# convert and reduce using party affiliation
dataframe = convert_party_affiliation(dataframe)

# plot voters in PC coordinates
scatter_voter = ax.scatter(
    dataframe["position_x"],
    dataframe["position_y"],
    s=1,
    c=dataframe[col_party],
    alpha=0.5,
    cmap="Set1",
)
legend1 = ax.legend(
    *scatter_voter.legend_elements(),
    loc="lower right",
    title="Parteipräferenz",
    bbox_to_anchor=(1.1, 0.0),
)
for i, text in enumerate(legend1.get_texts()):
    text.set_text(PARTY_DICTIONARY[i])
for lh in legend1.legendHandles:
    lh.set_alpha(1)

# save figure
fig.savefig("../fig/voter_distribution_party_affiliation.png")
