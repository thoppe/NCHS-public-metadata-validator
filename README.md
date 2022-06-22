# NCHS Public Metadata Validator

Validates National Center for Health Statistics ([NCHS](https://www.cdc.gov/nchs/index.htm)) metadata from [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS) through the [Federal Validator](https://dashboard.data.gov/validate). Uses GitHub actions to create two files for downstream consumption:


+ [NCHS_raw_datasets.csv](NCHS_raw_datasets.csv)
+ [NCHS_validiation_errors.csv](NCHS_validiation_errors.csv)


## Metadata Statistics

| Statistic | Value |
| :---      | ---:  |
| CDC datasets on [data.cdc.gov](https://data.cdc.gov/) | 876 |
| CDC/NCHS datasets on [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS)| **160** |
| CDC validation errors from the Federal Validator | 193 |
| CDC/NCHS validation errors from the Federal Validator | **47** |
| Unique CDC/NCHS datasets with validation errors | **25** |
| Last Updated | 2022-06-22 00:23:43 |


## Remaining 193 validation errors by category

| Category | Count |
| :---     | ---:  |
|BLANK|70|
|NCHS|47|
|Public Health Surveillance|13|
|Vaccinations|12|
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
|Disability & Health|1|
|Vision & Eye Health|1|
|Youth Risk Behaviors|1|