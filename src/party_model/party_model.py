"""Dynamic party model following Laver(2005).

Created using mesa.
"""
import matplotlib.pyplot as plt
import numpy as np
from mesa import Agent, Model
from mesa.time import BaseScheduler
from scipy.spatial import distance_matrix


class PartyAgent(Agent):
    """Agent representing one party."""

    def __init__(self, unique_id, model, initial_position, kind):
        """Initialize party agent.

        Args:
            unique_id: id
            model: party model
            initial_position: initial position in 2D space
            kind: the kind the party belongs to
        """
        super().__init__(unique_id, model)
        self.position = initial_position
        self.kind = kind

    def step(self):
        """Perform one update step for self.position.

        Raises:
            KeyError: if the kind is unknown
        """
        match self.kind:
            case "AGGREGATOR":
                # compute indices of own voters
                party_voters = np.where(
                    self.model.party_affiliation == self.unique_id
                )[0]
                # average across all its voter positions
                self.position = np.mean(
                    self.model.voter_positions[party_voters], axis=0
                )
                return
            case _:
                raise KeyError(
                    f"Party type {self.kind} is not included in step()"
                )


class PartyModel(Model):
    """Party model."""

    def __init__(self, party_positions, voter_positions):
        """Initialize the party model.

        Args:
            party_positions: initial party positions
            voter_positions: positions of voters in 2D space
        """
        super().__init__()
        self.num_agents = party_positions.shape[0]
        self.schedule = BaseScheduler(
            self
        )  # consider using SimultaneousActivation instead
        for i in range(self.num_agents):
            a = PartyAgent(i, self, party_positions[i], "AGGREGATOR")
            self.schedule.add(a)
        self.voter_positions = voter_positions

        self.party_affiliation = None
        self.vote_share = None
        self._update_party_affiliation()

    def step(self):
        """Perform one time step in mode.

        Implicitly updates the party affiliation of voters.
        """
        self.schedule.step()
        self._update_party_affiliation()

    def _update_party_affiliation(self):
        # distance matrix, shape (n_voter, n_parties)
        distances = distance_matrix(
            self.voter_positions, self._get_party_positions()
        )

        # party_affiliation is the smallest distance along second axis
        self.party_affiliation = np.argmin(distances, axis=1)

        # self.vote_share = count(self.party_affiliation)
        unique, unique_counts = np.unique(
            self.party_affiliation, return_counts=True
        )
        self.vote_share = np.zeros(self.num_agents)
        for index, count in zip(unique, unique_counts):
            self.vote_share[index] = count
        self.vote_share = self.vote_share / self.voter_positions.shape[0]
        return

    def _get_party_positions(self):
        party_positions = np.zeros((self.num_agents, 2))
        for i, party_agent in enumerate(self.schedule.agents):
            party_positions[i] = party_agent.position
        return party_positions

    def scatter_plot(self):
        """Plot party and voter positions with affiliation."""
        plt.figure()
        party_positions = self._get_party_positions()
        scatter_party = plt.scatter(
            party_positions[:, 0],
            party_positions[:, 1],
            c=range(self.num_agents),
        )
        plt.scatter(
            self.voter_positions[:, 0],
            self.voter_positions[:, 1],
            s=1,
            c=self.party_affiliation,
        )
        plt.legend(*scatter_party.legend_elements())
        plt.show()
