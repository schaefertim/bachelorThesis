"""Utility for politbarometer data."""
import numpy as np
import pandas as pd

from src.data_utility.party_dictionary import PARTY_MAPPING_POLITBAROMETER

filepath_politbarometer = "../data/ZA2391_v13-0-0.sav"
col_study = "v1"
col_participant = "v2"
col_month = "v3"
col_year = "v4"
col_party = "v6"
col_party_last = "v7"
cols_party_preference = [f"v{i}" for i in range(8, 15)]
col_left_right = "v22"

map_rating_int = {
    '-5 überhaupt nichts': -5,
    '-4': -4,
    '-3': -3,
    '-2': -2,
    '-1': -1,
    '0': 0,
    '+1': 1,
    '+2': 2,
    '+3': 3,
    '+4': 4,
    '+5 sehr viel': 5,
    'KA': np.NaN,
    'nicht erhoben': np.NaN,
}


def load_voter_data() -> pd.DataFrame:
    """Load opinions."""
    usecols = [
        col_study,
        col_participant,
        col_month,
        col_year,
        col_party,
        col_party_last,
    ] + cols_party_preference + [col_left_right]
    dataframe = pd.read_spss(filepath_politbarometer, usecols=usecols)
    return dataframe


def reduce_data(dataframe: pd.DataFrame, year=None, study=None, month=None) -> pd.DataFrame:
    if year is not None:
        dataframe = dataframe[dataframe[col_year] == year]
    if study is not None:
        dataframe = dataframe[dataframe[col_study] == study]
    if month is not None:
        dataframe = dataframe[dataframe[col_month] == month]

    dataframe[cols_party_preference] = dataframe[cols_party_preference].apply(lambda x: x.cat.codes)
    for col_party_preference in cols_party_preference:
        dataframe = dataframe[dataframe[col_party_preference] != 0]
        dataframe = dataframe[dataframe[col_party_preference] != 99]
    return dataframe


def calculate_voter_position(position_party, dataframe_voter) -> pd.DataFrame:
    for i in range(2):  # x,y
        nominator = 0
        denominator = 0
        for p, col_party_preference in enumerate(cols_party_preference):
            nominator += np.exp(dataframe_voter[col_party_preference]) * position_party[PARTY_MAPPING_POLITBAROMETER[p], i]
            denominator += np.exp(dataframe_voter[col_party_preference])
        dataframe_voter[f'position_{"x" if i==0 else "y"}'] = nominator / denominator
    return dataframe_voter
