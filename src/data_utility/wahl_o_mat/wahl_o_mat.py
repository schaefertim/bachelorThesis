"""Data utility for Wahl-O-Mat data."""
from os import path

import numpy as np
import pandas as pd

filepath_wahl_o_mat = "../data/wahl_o_mat_2017"


def load_opinion(n_parties=None, replace_neutral=True) -> pd.DataFrame:
    """Load opinions of parties."""
    filepath_opinion = path.join(filepath_wahl_o_mat, "opinion.json")
    data = pd.read_json(filepath_opinion)

    # replace answer 2 with 0.5, since this is the neutral position
    if replace_neutral:
        data['answer'] = data['answer'].replace(to_replace=2, value=0.5)

    if n_parties is not None:
        data = data.loc[lambda df: df['party'] < n_parties]

    return data


def load_statement() -> pd.DataFrame:
    """Load statements."""
    filepath_statement = path.join(filepath_wahl_o_mat, "statement.json")
    data = pd.read_json(filepath_statement)
    return data


def opinion_to_array(opinions: pd.DataFrame):
    """Transform opinion dataframe to array."""
    n_parties = len(opinions['party'].unique())
    n_statements = len(opinions['statement'].unique())
    party_positions = np.zeros((n_parties, n_statements))
    for row in opinions.itertuples():
        party_positions[row.party, row.statement] = row.answer
    return party_positions