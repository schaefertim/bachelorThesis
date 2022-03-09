"""Data utility for Wahl-O-Mat data."""
from os import path

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

filepath_wahl_o_mat = "../data/wahl_o_mat_2017"


def load_opinion(n_parties=None, replace_neutral=True) -> pd.DataFrame:
    """Load opinions of parties.

    Args:
        n_parties: number of parties
        replace_neutral: whether to replace the neutral answer 2 by 0.5

    Returns:
        dataframe of parties' answers
    """
    filepath_opinion = path.join(filepath_wahl_o_mat, "opinion.json")
    data = pd.read_json(filepath_opinion)

    # replace answer 2 with 0.5, since this is the neutral position
    if replace_neutral:
        data["answer"] = data["answer"].replace(to_replace=2, value=0.5)

    if n_parties is not None:
        data = data.loc[lambda df: df["party"] < n_parties]

    return data


def load_statement() -> pd.DataFrame:
    """Load statements.

    Returns:
        dataframe of the statements of the questionnaire
    """
    filepath_statement = path.join(filepath_wahl_o_mat, "statement.json")
    data = pd.read_json(filepath_statement)
    return data


def opinion_to_array(opinions: pd.DataFrame):
    """Transform opinion dataframe to array.

    Args:
        opinions: dataframe of the loaded opinions of the parties

    Returns:
        array of opinions, shape [n_party, n_statement]
    """
    n_parties = len(opinions["party"].unique())
    n_statements = len(opinions["statement"].unique())
    party_positions = np.zeros((n_parties, n_statements))
    for row in opinions.itertuples():
        party_positions[row.party, row.statement] = row.answer
    return party_positions


def perform_pca(party_positions):
    """Perform a PCA with 2 components.

    Args:
        party_positions: array of party positions

    Returns:
        party_positions in pca dimensions, pca
    """
    pca = PCA(n_components=2).fit(party_positions)
    party_positions_pca = np.einsum(
        "ps,cs->pc", party_positions, pca.components_
    )
    return party_positions_pca, pca


def print_pca_significant_statements(pca, dataframe_statement):
    """Calculate and print the most important statements of pca directions.

    Args:
        pca: PCA as previously calculated
        dataframe_statement: statement data
    """
    pca_argsort = np.argsort(np.abs(pca.components_), axis=1)[:, ::-1]
    print("statements from first PCA")
    for statement in pca_argsort[0, :5]:
        print(
            statement,
            dataframe_statement.iloc[statement]["label"],
            ": ",
            dataframe_statement.iloc[statement]["text"],
            pca.components_[0, statement],
        )

    print("\nstatements from second PCA")
    for statement in pca_argsort[1, :5]:
        print(
            statement,
            dataframe_statement.iloc[statement]["label"],
            ": ",
            dataframe_statement.iloc[statement]["text"],
            pca.components_[1, statement],
        )
