"""Party dictionary mapping all indices to a global party index."""

# dictionary to globally identify parties by index
PARTY_DICTIONARY = {
    0: "CDU/CSU",
    1: "SPD",
    2: "AfD",
    3: "FDP",
    4: "DIE LINKE",
    5: "GRÜNE",
}

# mapping for the indices of the Wahl-O-Mat data of 2017 to global index
PARTY_MAPPING_WAHL_O_MAT_2017 = {
    0: 0,
    1: 1,
    2: 4,
    3: 5,
    4: 3,
    5: 2,
}

# mapping for the indices of the politbarometer indices regarding party
# preference to the global index
PARTY_MAPPING_POLITBAROMETER = [
    1,  # SPD
    0,  # CDU
    0,  # CSU
    3,  # FDP
    5,  # GRÜNE
    2,  # AfD
    4,  # DIE LINKEN
]
