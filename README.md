# NCHS Public Metadata Validator

Validates National Center for Health Statistics ([NCHS](https://www.cdc.gov/nchs/index.htm)) metadata from [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS) through the [Federal Validator](https://dashboard.data.gov/validate). Uses GitHub actions to create two files for downstream consumption:


+ [NCHS_raw_datasets.csv](NCHS_raw_datasets.csv)
+ [NCHS_validiation_errors.csv](NCHS_validiation_errors.csv)


## Metadata Statistics

| Statistic | Value |
| :---      | ---:  |
| CDC datasets on [data.cdc.gov](https://data.cdc.gov/) | 929 |
| CDC/NCHS datasets on [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS)| **147** |
| CDC validation errors from the Federal Validator | 211 |
| CDC/NCHS validation errors from the Federal Validator | **14** |
| Unique CDC/NCHS datasets with validation errors | **6** |
| Last Updated | 2022-12-25 00:21:18 |


## Remaining 211 validation errors by category

| Category | Count |
| :---     | ---:  |
|BLANK|75|
|Vaccinations|38|
|Public Health Surveillance|24|
|NCHS|14|
|Case Surveillance|10|
|Administrative|6|
|Environmental Health & Toxicology|6|
|Health Statistics|5|
|Laboratory Surveillance|5|
|Global Health|5|
|Foodborne, Waterborne, and Related Diseases|5|
|NNDSS|4|
|Policy Surveillance|4|
|Pregnancy & Vaccination|3|
|Tobacco Use|2|
|Child Vaccinations|2|
|Disability & Health|1|
|Vision & Eye Health|1|
|Youth Risk Behaviors|1|