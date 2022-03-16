"""Color the voter distribution from left to right."""
import matplotlib.pyplot as plt

from src.data_utility.party_dictionary import PARTY_DICTIONARY
from src.data_utility.politbarometer.politbarometer import (
    calculate_voter_position,
    col_party,
    convert_party_affiliation,
    load_voter_data,
    reduce_data,
)
from src.data_utility.wahl_o_mat.wahl_o_mat import (
    load_opinion,
    load_statement,
    opinion_to_array,
    perform_pca,
)

# load party data
dataframe_statement = load_statement()
party_positions = opinion_to_array(load_opinion(n_parties=6))

# compute pca and new party positions
party_positions, pca = perform_pca(party_positions)

# plot party positions
fig, ax = plt.subplots()
ax.scatter(party_positions[:, 0], party_positions[:, 1])
for party in range(6):
    ax.text(
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

# convert and reduce
dataframe = convert_party_affiliation(dataframe)

# plot voters in PC coordinates
scatter_voter = ax.scatter(
    dataframe["position_x"],
    dataframe["position_y"],
    s=1,
    c=dataframe[col_party],
    cmap="Set1",
)
legend1 = ax.legend(
    *scatter_voter.legend_elements(),
    loc="upper right",
    title="Parteipräferenz",
    bbox_to_anchor=(1.1, 1.0),
)
for i, text in enumerate(legend1.get_texts()):
    text.set_text(PARTY_DICTIONARY[i])

fig.savefig("../fig/voter_distribution_party_affiliation.png")
