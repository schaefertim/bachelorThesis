"""Party dictionary."""

# dictionary to identify parties by index
PARTY_DICTIONARY = {
    0: "CDU/CSU",
    1: "SPD",
    2: "AfD",
    3: "FDP",
    4: "DIE LINKE",
    5: "GRÜNE",
}

PARTY_MAPPING_WAHL_O_MAT_2017 = {
    0: 0,
    1: 1,
    2: 4,
    3: 5,
    4: 3,
    5: 2,
}

PARTY_MAPPING_POLITBAROMETER = [
    1,  # SPD
    0,  # CDU
    0,  # CSU
    3,  # FDP
    5,  # GRÜNE
    2,  # AfD
    4,  # DIE LINKEN
]
