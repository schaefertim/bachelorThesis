"""Test the different kinds of party models."""

# load party positions from file
from datetime import datetime

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

# perform 1000 steps in party model and measure execution time
tic = datetime.now()
for _ in range(1000):
    party_model.step()
toc = datetime.now()
print(f"Execution time of 1000 steps: {toc - tic}")

# plot
party_model.scatter_plot()
