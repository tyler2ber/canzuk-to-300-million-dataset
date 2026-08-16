import pandas as pd

# data
regions_nation = {
    "Canada": 41417056,
    "Australia": 27262902,
    "New Zealand": 5361300,
    "UK": 70011675
}
regions_nation_total = sum(regions_nation.values())

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

print(df_projections.head())

# PROJECTIONS
# ..