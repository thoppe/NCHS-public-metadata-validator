"""
Cross reference the data from the Federal Validator (FV):
https://dashboard.data.gov/validate

Against the Socrata output from data.json. FV returns results based
off of numerical order from data.json, need to cross-reference and return
only NCHS results in a nice CSV. Program outputs results to CSV:
NCHS_validiation_errors.csv
"""

import json
from pathlib import Path
import pandas as pd

# Presume NCHS_raw_datasets.csv exists already
# (computed from P0_filter_NCHS_data.py)
f_csv = Path("NCHS_raw_datasets.csv")
assert f_csv.exists()
df = pd.read_csv(f_csv).set_index("data_json_order")

# Load the validation file and check if it exists
f_validation = Path("federal_validation.json")
assert f_validation.exists()
JS = json.load(open(f_validation))
errors = JS["errors"]


# Parse the JSON file and keep only the datasets from NCHS
data = []
for key in errors:

    # federal_validation.json stores as string
    # If the key is not in the df then it's not NCHS
    if int(key) not in df.index.values:
        continue

    for name in errors[key]:

        item = errors[key][name]

        # Validation error text can be found in both 'errors' and
        # 'sub-fields'. Collect all text regardless
        text = []
        for row in item:
            text.extend(item[row])
        text = "; ".join(text)

        info = df.loc[int(key)]

        # Build the output columns
        data.append(
            {
                "data_json_order": key,
                "field": name,
                "value": info[name],
                "identifier": info["identifier"],
                "title": info["title"],
                "validation_text": text,
            }
        )

# Create and save a dataframe
errors = pd.DataFrame(data).set_index("data_json_order")
errors.to_csv("NCHS_validiation_errors.csv")

print(errors)
