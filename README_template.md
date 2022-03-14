# NCHS Public Metadata Validator

Validates National Center for Health Statistics ([NCHS](https://www.cdc.gov/nchs/index.htm)) metadata from [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS) through the [Federal Validator](https://dashboard.data.gov/validate). Uses GitHub actions to create two files for downstream consumption:


+ [NCHS_raw_datasets.csv](NCHS_raw_datasets.csv)
+ [NCHS_validiation_errors.csv](NCHS_validiation_errors.csv)


## Metadata Statistics


| Statistic | Value |
| :---      | ---:  |
| CDC datasets on [data.cdc.gov](https://data.cdc.gov/) | {n_CDC_datasets} |
| CDC/NCHS datasets on [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS)| **{n_NCHS_datasets}** |
| CDC validation errors from the Federal Validator | {n_CDC_errors} |
| CDC/NCHS validation errors from the Federal Validator | **{n_NCHS_errors}** |
| Unique CDC/NCHS datasets with validation errors | **{n_NCHS_error_datasets}** |
| Last Updated | {data_last_updated} |