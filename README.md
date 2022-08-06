# NCHS Public Metadata Validator

Validates National Center for Health Statistics ([NCHS](https://www.cdc.gov/nchs/index.htm)) metadata from [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS) through the [Federal Validator](https://dashboard.data.gov/validate). Uses GitHub actions to create two files for downstream consumption:


+ [NCHS_raw_datasets.csv](NCHS_raw_datasets.csv)
+ [NCHS_validiation_errors.csv](NCHS_validiation_errors.csv)


## Metadata Statistics

| Statistic | Value |
| :---      | ---:  |
| CDC datasets on [data.cdc.gov](https://data.cdc.gov/) | 881 |
| CDC/NCHS datasets on [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS)| **137** |
| CDC validation errors from the Federal Validator | 147 |
| CDC/NCHS validation errors from the Federal Validator | **1** |
| Unique CDC/NCHS datasets with validation errors | **1** |
| Last Updated | 2022-08-06 00:21:26 |


## Remaining 147 validation errors by category

| Category | Count |
| :---     | ---:  |
|BLANK|69|
|Vaccinations|13|
|Public Health Surveillance|13|
|Case Surveillance|7|
|Administrative|6|
|Global Health|5|
|Health Statistics|5|
|Policy Surveillance|4|
|NNDSS|4|
|Laboratory Surveillance|4|
|Environmental Health & Toxicology|4|
|Pregnancy & Vaccination|3|
|Foodborne, Waterborne, and Related Diseases|2|
|Tobacco Use|2|
|Child Vaccinations|2|
|NCHS|1|
|Disability & Health|1|
|Vision & Eye Health|1|
|Youth Risk Behaviors|1|