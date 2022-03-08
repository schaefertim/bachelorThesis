"""Handling the data from Politbarometer."""

from src.data_utility.politbarometer.politbarometer import load_voter_data

dataframe = load_voter_data()

print("no rows=", dataframe.count() + 1)
print(dataframe.head(3))
