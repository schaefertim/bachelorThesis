"""Test the party model."""
import numpy as np

from src.party_model.party_model import PartyModel

# load party positions from file
party_positions_pca = np.load("../data/saved/party_positions_pca.npy")

# load voter positions from file
voter_positions = np.load("../data/saved/voter_positions.npy")

# initialize party model
party_model = PartyModel(
    party_positions=party_positions_pca[:6], voter_positions=voter_positions
)

# plot initial party model
# print(party_model.vote_share)
party_model.scatter_plot()

# perform one step in party model
for _ in range(100):
    party_model.step()

# plot party model after one step
party_model.scatter_plot()
