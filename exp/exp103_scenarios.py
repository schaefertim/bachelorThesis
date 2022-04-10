"""Experiment the scenarios in Laver(2005) with the german data."""

from os import path

import numpy as np

from src.party_model.party_model import PartyModel

# settings for all experiments
settings = [
    {
        "kinds": ["AGGREGATOR" for _ in range(6)],
        "fig_name": "fig_laver_aggregator6.png",
    },
    {
        "kinds": ["HUNTER" for _ in range(6)],
        "fig_name": "fig_laver_hunter6.png",
    },
    {
        "kinds": ["HUNTER" for _ in range(2)],
        "fig_name": "fig_laver_hunter2.png",
    },
    {
        "kinds": ["AGGREGATOR" for _ in range(5)] + ["HUNTER"],
        "fig_name": "fig_laver_aggregator5_hunter.png",
    },
    {
        "kinds": ["AGGREGATOR" for _ in range(5)] + ["PREDATOR"],
        "fig_name": "fig_laver_aggregator5_predator.png",
    },
    {
        "kinds": ["AGGREGATOR" for _ in range(4)] + ["HUNTER", "HUNTER"],
        "fig_name": "fig_laver_aggregator4_hunter2.png",
    },
    {
        "kinds": ["AGGREGATOR" for _ in range(4)] + ["PREDATOR", "PREDATOR"],
        "fig_name": "fig_laver_aggregator4_predator2.png",
    },
    {
        "kinds": ["AGGREGATOR" for _ in range(4)] + ["PREDATOR", "HUNTER"],
        "fig_name": "fig_laver_aggregator4_predator_hunter.png",
    },
    {
        "kinds": ["HUNTER" for _ in range(5)] + ["PREDATOR"],
        "fig_name": "fig_laver_hunter5_predator.png",
    },
]


# load party positions from file
party_positions_pca = np.load("../data/saved/party_positions_pca.npy")

# load voter positions from file
voter_positions = np.load("../data/saved/voter_positions.npy")

# for each element in settings run experiment
for setting in settings:
    n_parties = len(setting["kinds"])
    # initialize party model
    party_model = PartyModel(
        party_positions=party_positions_pca[:n_parties],
        voter_positions=voter_positions,
        kinds=setting["kinds"],
    )

    # run 1000 steps
    for _ in range(1000):
        party_model.step()

    # save plot
    fig_path = path.join("../fig", setting["fig_name"])
    party_model.scatter_plot(filename=fig_path)
