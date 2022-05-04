# NCHS Public Metadata Validator

Validates National Center for Health Statistics ([NCHS](https://www.cdc.gov/nchs/index.htm)) metadata from [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS) through the [Federal Validator](https://dashboard.data.gov/validate). Uses GitHub actions to create two files for downstream consumption:


+ [NCHS_raw_datasets.csv](NCHS_raw_datasets.csv)
+ [NCHS_validiation_errors.csv](NCHS_validiation_errors.csv)


## Metadata Statistics

| Statistic | Value |
| :---      | ---:  |
| CDC datasets on [data.cdc.gov](https://data.cdc.gov/) | 858 |
| CDC/NCHS datasets on [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS)| **135** |
| CDC validation errors from the Federal Validator | 137 |
| CDC/NCHS validation errors from the Federal Validator | **0** |
| Unique CDC/NCHS datasets with validation errors | **0** |
| Last Updated | 2022-05-04 00:19:18 |


## Remaining 137 validation errors by category

| Category | Count |
| :---     | ---:  |
|BLANK|67|
|Vaccinations|12|
|Public Health Surveillance|10|
|Administrative|6|
|Case Surveillance|5|
|Global Health|5|
|Health Statistics|5|
|Policy Surveillance|4|
|Environmental Health & Toxicology|4|
|NNDSS|4|
|Pregnancy & Vaccination|3|
|Laboratory Surveillance|3|
|Foodborne, Waterborne, and Related Diseases|2|
|Tobacco Use|2|
|Child Vaccinations|2|
|Disability & Health|1|
|Vision & Eye Health|1|
|Youth Risk Behaviors|1|