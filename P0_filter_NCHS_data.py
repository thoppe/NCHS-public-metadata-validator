"""
Filters metadata from data.cdc.gov so only NCHS datasets remain,
returns a nicely formated CSV. Saves the dataframe to a file for
future analysis.
"""

import json
from pathlib import Path
import pandas as pd


# Presume data.json exists already (should be downloaded from github action)
f_src = Path("data.json")
assert f_src.exists()

# Parse the JSON file and keep only the datasets
JS = json.load(open(f_src))
df = pd.DataFrame(JS["dataset"])

# Set the index on the landingPage
df = df.set_index("landingPage")

# Some datasets may not have a "theme" so fill them in with blanks
# The category (internally theme) is a list with a single item
# turn this into a single text field
df["category"] = df["theme"].fillna(" ").apply(lambda x: x[0])

# Keep the dataset order for validation against dashboard.data.gov
df["data_json_order"] = range(len(df))

# Only keep the datasets that belong to NCHS
idx = df["category"] == "NCHS"
df = df[idx]

df.to_csv("NCHS_raw_datasets.csv")
