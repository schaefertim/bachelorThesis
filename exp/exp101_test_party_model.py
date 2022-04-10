"""Test the party model.

Additionally, measure the execution time as a benchmark case.
"""
from datetime import datetime

import numpy as np

from src.party_model.party_model import PartyModel

# load party positions from file
party_positions_pca = np.load("../data/saved/party_positions_pca.npy")
print("party_positions_pca.shape", party_positions_pca.shape)

# load voter positions from file
voter_positions = np.load("../data/saved/voter_positions.npy")
print("voter_positions.shape", voter_positions.shape)

# initialize party model
party_model = PartyModel(
    party_positions=party_positions_pca[:6], voter_positions=voter_positions
)

# plot initial party model
party_model.scatter_plot()

# perform 1000 steps in party model and measure execution time
tic = datetime.now()
for _ in range(100):
    party_model.step()
toc = datetime.now()
print(f"Execution time of 1000 steps: {toc-tic}")

# plot party model afterwards
party_model.scatter_plot()
