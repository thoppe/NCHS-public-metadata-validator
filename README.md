# NCHS Public Metadata Validator

Validates National Center for Health Statistics ([NCHS](https://www.cdc.gov/nchs/index.htm)) metadata from [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS) through the [Federal Validator](https://dashboard.data.gov/validate). Uses GitHub actions to create two files for downstream consumption:


+ [NCHS_raw_datasets.csv](NCHS_raw_datasets.csv)
+ [NCHS_validiation_errors.csv](NCHS_validiation_errors.csv)


## Metadata Statistics

| Statistic | Value |
| :---      | ---:  |
| CDC datasets on [data.cdc.gov](https://data.cdc.gov/) | 958 |
| CDC/NCHS datasets on [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS)| **154** |
| CDC validation errors from the Federal Validator | 199 |
| CDC/NCHS validation errors from the Federal Validator | **8** |
| Unique CDC/NCHS datasets with validation errors | **6** |
| Last Updated | 2023-06-10 00:20:27 |


## Remaining 199 validation errors by category

| Category | Count |
| :---     | ---:  |
|BLANK|68|
|Vaccinations|38|
|Public Health Surveillance|22|
|Case Surveillance|8|
|NCHS|8|
|Laboratory Surveillance|7|
|Foodborne, Waterborne, and Related Diseases|7|
|Administrative|6|
|Environmental Health & Toxicology|6|
|Health Statistics|5|
|Global Health|5|
|NNDSS|4|
|Policy Surveillance|4|
|Pregnancy & Vaccination|3|
|Child Vaccinations|2|
|Tobacco Use|2|
|Vision & Eye Health|1|
|Models|1|
|Disability & Health|1|
|Youth Risk Behaviors|1|