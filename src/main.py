import pandas as pd

# data
nation_populations = {
    "Canada": 41417056,
    "Australia": 27262902,
    "New Zealand": 5361300,
    "UK": 70011675
}
nation_populations_total = sum(nation_populations.values())

# projections data w/ df_projections
projections = {
    "Canada": -1,
    "Australia": -1,
    "New Zealand": -1,
    "UK": -1
}
projections_total = -1

df_projections = pd.DataFrame(columns=
    [
        "GEN",
        "Canada",
        "Australia",
        "New Zealand",
        "UK",
        "total_population"
    ]
).astype(
    {
        "GEN": "int64",
        "Canada": "int64",
        "Australia": "int64",
        "New Zealand": "int64",
        "UK": "int64",
        "total_population": "int64"
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
    if projections_total == -1:

        # gen (init)
        gen_counter = 1

        # projections (init)
        for projection in projections:
            projections[projection] = nation_populations[projection]

        # projections total (init)
        projections_total = nation_populations_total

    else:

        # gen
        gen_counter += 1

        # projections
        for projection in projections:
            projections[projection] = (projections[projection] / 2) * 3

        # projections total
        projections_total = sum(projections.values())

    # PRINT
    print(f"====> canzuk_nations(gen{gen_counter}): {round(projections_total):,}")
    for projection in projections:
        print(f"{'✔ ' if projections[projection] >= 300000000 else '- '} {round(projections[projection]):,} in {projection}")

    # ...and update df_projections