"""Handling the data from Politbarometer."""

import pandas as pd

filepath = "../../data/ZA2391_v13-0-0.sav"
col_study = "v1"
col_participant = "v2"
col_month = "v3"
col_year = "v4"
col_party = "v6"
col_party_last = "v7"
col_spd = "v8"
col_cdu = "v9"
col_left_right = "v22"
usecols = [col_study, col_participant, col_month, col_year, col_party, col_party_last, col_spd, col_cdu, col_left_right]
# usecols = [f"v{i}" for i in range(1, 10)]
dataframe = pd.read_spss(filepath, usecols=usecols)

print("no rows=", dataframe.count() + 1)
print(dataframe.head(3))


