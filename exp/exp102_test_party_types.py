"""Test the different kinds of party models."""

# load party positions from file
import numpy as np

from src.party_model.party_model import PartyModel

party_positions_pca = np.load("../data/saved/party_positions_pca.npy")

# load voter positions from file
voter_positions = np.load("../data/saved/voter_positions.npy")

# initialize party model
party_model = PartyModel(
    party_positions=party_positions_pca[:6],
    voter_positions=voter_positions,
    kinds=[
        "AGGREGATOR",
        "HUNTER",
        "HUNTER",
        "PREDATOR",
        "PREDATOR",
        "STICKER",
    ],
)

for _ in range(1000):
    party_model.step()

party_model.scatter_plot()
