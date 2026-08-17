import pandas as pd

# data
nation_populations = {
    "Canada": 41417056,
    "Australia": 27262902,
    "New Zealand": 5361300,
    "UK": 70011675
}

# projections data w/ df_projections
projections = {
    "Canada": -1,
    "Australia": -1,
    "New Zealand": -1,
    "UK": -1
}

df_projections = pd.DataFrame(columns=
    [
        "GEN",
        "Canada",
        "Australia",
        "New Zealand",
        "UK"
    ]
).astype(
    {
        "GEN": "int64",
        "Canada": "int64",
        "Australia": "int64",
        "New Zealand": "int64",
        "UK": "int64"
    }
)

# PROJECTIONS

def all_reached_300million():
    for projection in projections:
        if projections[projection] < 300000000:
            return False
    return True

print("\nPROJECTIONS")

gen_counter = 0
while not all_reached_300million():

    # CALCULATE
    if gen_counter == 0:

        # gen (init)
        gen_counter = 1

        # projections (init)
        for projection in projections:
            projections[projection] = nation_populations[projection]

    else:

        # gen
        gen_counter += 1

        # projections
        for projection in projections:
            if projections[projection] < 300000000:
                projections[projection] = (projections[projection] / 2) * 3

    # PRINT
    print(f"====> canzuk_nations(gen{gen_counter})")
    for projection in projections:
        print(f"{'✔ ' if projections[projection] >= 300000000 else '- '} {round(projections[projection]):,} in {projection}")

    # ...and update df_projections
    df_projections.loc[len(df_projections)] = [
        gen_counter,
        round(projections["Canada"]),
        round(projections["Australia"]),
        round(projections["New Zealand"]),
        round(projections["UK"])
    ]

print("") # lul
df_projections.to_csv("dataset/canzuk-to-300-million.csv", index=False)