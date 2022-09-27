# NCHS Public Metadata Validator

Validates National Center for Health Statistics ([NCHS](https://www.cdc.gov/nchs/index.htm)) metadata from [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS) through the [Federal Validator](https://dashboard.data.gov/validate). Uses GitHub actions to create two files for downstream consumption:


+ [NCHS_raw_datasets.csv](NCHS_raw_datasets.csv)
+ [NCHS_validiation_errors.csv](NCHS_validiation_errors.csv)


## Metadata Statistics

| Statistic | Value |
| :---      | ---:  |
| CDC datasets on [data.cdc.gov](https://data.cdc.gov/) | 886 |
| CDC/NCHS datasets on [data.cdc.gov](https://data.cdc.gov/browse?category=NCHS)| **142** |
| CDC validation errors from the Federal Validator | 148 |
| CDC/NCHS validation errors from the Federal Validator | **2** |
| Unique CDC/NCHS datasets with validation errors | **2** |
| Last Updated | 2022-09-27 00:28:42 |


## Remaining 148 validation errors by category

| Category | Count |
| :---     | ---:  |
|BLANK|69|
|Public Health Surveillance|13|
|Vaccinations|12|
|Case Surveillance|8|
|Administrative|6|
|Global Health|5|
|Health Statistics|5|
|Policy Surveillance|4|
|NNDSS|4|
|Laboratory Surveillance|4|
|Environmental Health & Toxicology|4|
|Pregnancy & Vaccination|3|
|NCHS|2|
|Foodborne, Waterborne, and Related Diseases|2|
|Tobacco Use|2|
|Child Vaccinations|2|
|Disability & Health|1|
|Vision & Eye Health|1|
|Youth Risk Behaviors|1|