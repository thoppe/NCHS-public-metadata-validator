"""
Cross-reference the data from the Federal Validator (FV):
https://dashboard.data.gov/validate

against the Socrata output from data.json. FV returns results based
off of numerical order from data.json, need to cross-reference and return
only NCHS results in a nice CSV. Program outputs results to CSV:
NCHS_validiation_errors.csv
"""

import json
from pathlib import Path
import pandas as pd

# Presume NCHS_raw_datasets.csv exists already
# (computed from P0_filter_NCHS_data.py)
f_csv = Path("CDC_raw_datasets.csv")
assert f_csv.exists()
df = pd.read_csv(f_csv).set_index("data_json_order")

# Load the validation file and check if it exists
f_validation = Path("federal_validation.json")
assert f_validation.exists()
JS = json.load(open(f_validation))

# If there are no errors, return an empty list
if "errors" in JS:
    errors = JS["errors"]
else:
    errors = []

# Parse the JSON file and keep only the datasets from NCHS
data = []
for key in errors:

    # federal_validation.json stores as string
    # If the key is not in the df then it's not NCHS
    # if int(key) not in df.index.values:
    #    continue

    for name in errors[key]:

        item = errors[key][name]

        # Validation error text can be found in both 'errors' and
        # 'sub-fields'. Collect all text regardless
        text = []
        for row in item:
            text.extend(item[row])
        text = "; ".join(text)

        info = df.loc[int(key)]

        # contactPoint is stored as contactPoint.hasEmail
        if ".hasEmail" in name:
            name = name.replace(".hasEmail", "")
        value = info[name]

        # Use a custom string for a missing category
        category = info["category"].strip()
        if not category:
            category = "BLANK"

        # Build the output columns
        data.append(
            {
                "data_json_order": key,
                "field": name,
                "value": value,
                "identifier": info["identifier"],
                "title": info["title"],
                "category": category,
                "validation_text": text,
            }
        )

# Create and save a dataframe

if data:
    errors = pd.DataFrame(data)
else:
    # If there are no errors, create a mock dataframe
    mock_cols = [
        "data_json_order",
        "field",
        "value",
        "identifier",
        "title",
        "category",
        "validation_text",
    ]
    errors = pd.DataFrame(columns=mock_cols)

# Align the index to the order returned by the FV
errors = errors.set_index("data_json_order")

# Show the errors for all CIOs
print(errors.groupby("category").size().sort_values(ascending=False))

# Save (for later consumption) all CDC errors
errors.to_csv("CDC_validiation_errors.csv")

# Save only NCHS errors
errors = errors[errors["category"] == "NCHS"]
errors.to_csv("NCHS_validiation_errors.csv")
