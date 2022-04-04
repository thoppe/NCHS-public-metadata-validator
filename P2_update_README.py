"""
Updates the README when the github action is run to account for the
current stats. Uses "README_template.md" to build "README.md".
"""

import json
from pathlib import Path
import pandas as pd
from datetime import datetime

f_README_template = Path("README_template.md")
f_NCHS_errors_csv = Path("NCHS_validiation_errors.csv")
f_NCHS_csv = Path("NCHS_raw_datasets.csv")
f_CDC_json = Path("data.json")
f_CDC_errors = Path("CDC_validiation_errors.csv")

# Check to make sure these files exist before starting
assert f_README_template.exists()
assert f_NCHS_errors_csv.exists()
assert f_NCHS_csv.exists()
assert f_CDC_json.exists()
assert f_CDC_errors.exists()

# This does not need to exist already
f_README_output = Path("README.md")

# Count the number of CDC datasets
n_CDC_datasets = len(json.load(open(f_CDC_json))["dataset"])

# Count the number of CDC/NCHS datasets
n_NCHS_datasets = len(pd.read_csv(f_NCHS_csv))

# Count the number of total CDC errors in the validator
df_CDC = pd.read_csv(f_CDC_errors)
n_CDC_errors = len(df_CDC)

# Count the number of total CDC/NCHS errors in the validator
df = pd.read_csv(f_NCHS_errors_csv)
n_NCHS_errors = len(df)

# Count the number of unique CDC/NCHS datasets with errors
n_NCHS_error_datasets = len(df["identifier"].unique())

with open(f_README_template) as FIN:
    template = FIN.read()


# Create a table with the remaining errors listed
table_validation_errors = []
counts = df_CDC.groupby("category").size().sort_values(ascending=False)
for name, value in counts.iteritems():
    row_text = f"|{name}|{value}|"
    table_validation_errors.append(row_text)
table_validation_errors = "\n".join(table_validation_errors)

stats = {
    "n_CDC_datasets": n_CDC_datasets,
    "n_NCHS_datasets": n_NCHS_datasets,
    "n_CDC_errors": n_CDC_errors,
    "n_NCHS_errors": n_NCHS_errors,
    "n_NCHS_error_datasets": n_NCHS_error_datasets,
    "data_last_updated": datetime.now().isoformat(" ", "seconds"),
    "table_validation_errors": table_validation_errors,
}

with open(f_README_output, "w") as FOUT:
    FOUT.write(template.format(**stats))
