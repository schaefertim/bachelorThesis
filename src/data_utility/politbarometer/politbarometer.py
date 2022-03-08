"""Utility for politbarometer data."""
import pandas as pd

filepath_politbarometer = "../../data/ZA2391_v13-0-0.sav"
col_study = "v1"
col_participant = "v2"
col_month = "v3"
col_year = "v4"
col_party = "v6"
col_party_last = "v7"
cols_party_preferance = [f"v{i}" for i in range(8, 15)]
col_left_right = "v22"


def load_voter_data() -> pd.DataFrame:
    """Load opinions."""
    usecols = [
        col_study,
        col_participant,
        col_month,
        col_year,
        col_party,
        col_party_last,
    ] + cols_party_preferance + [col_left_right]
    dataframe = pd.read_spss(filepath_politbarometer, usecols=usecols)
    return dataframe
