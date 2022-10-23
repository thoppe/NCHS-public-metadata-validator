# NCHS Public Metadata Validator

Validates National Center for Health Statistics ([NCHS](https://www.cdc.gov/nchs/index.htm)) metadata from [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS) through the [Federal Validator](https://dashboard.data.gov/validate). Uses GitHub actions to create two files for downstream consumption:


+ [NCHS_raw_datasets.csv](NCHS_raw_datasets.csv)
+ [NCHS_validiation_errors.csv](NCHS_validiation_errors.csv)


## Metadata Statistics

| Statistic | Value |
| :---      | ---:  |
| CDC datasets on [data.cdc.gov](https://data.cdc.gov/) | 900 |
| CDC/NCHS datasets on [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS)| **143** |
| CDC validation errors from the Federal Validator | 183 |
| CDC/NCHS validation errors from the Federal Validator | **2** |
| Unique CDC/NCHS datasets with validation errors | **2** |
| Last Updated | 2022-10-23 00:32:54 |


## Remaining 183 validation errors by category

| Category | Count |
| :---     | ---:  |
|BLANK|75|
|Vaccinations|32|
|Public Health Surveillance|19|
|Case Surveillance|8|
|Administrative|6|
|Environmental Health & Toxicology|6|
|Health Statistics|5|
|Laboratory Surveillance|5|
|Global Health|5|
|NNDSS|4|
|Policy Surveillance|4|
|Pregnancy & Vaccination|3|
|Foodborne, Waterborne, and Related Diseases|2|
|NCHS|2|
|Tobacco Use|2|
|Child Vaccinations|2|
|Disability & Health|1|
|Vision & Eye Health|1|
|Youth Risk Behaviors|1|