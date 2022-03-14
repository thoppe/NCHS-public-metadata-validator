# NCHS Public Metadata Validator

Validates National Center for Health Statistics ([NCHS](https://www.cdc.gov/nchs/index.htm)) metadata from [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS) through the [Federal Validator](https://dashboard.data.gov/validate). Uses GitHub actions to create two files for downstream consumption:


+ [NCHS_raw_datasets.csv](NCHS_raw_datasets.csv)
+ [NCHS_validiation_errors.csv](NCHS_validiation_errors.csv)


## Metadata Statistics


+ Number of datasets on [data.cdc.gov](https://data.cdc.gov/): {n_CDC_datasets}
+ Number of NCHS datasets on [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS): {n_NCHS_datasets}

+ Number of CDC validation errors from the Federal Validator: {n_CDC_errors}
+ Number of NCHS validation errors from the Federal Validator: {n_NCHS_errors}
+ Number of unique NCHS datasets with validation errors from the Federal Validator: {n_NCHS_errors}

+ Last Updated: {data_last_updated}