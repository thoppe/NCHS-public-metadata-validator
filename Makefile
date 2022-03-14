# Makefile only for development

lint:
	black *.py
	yamllint .github/workflows/parse-CDC-metadata.yml	

edit:
	emacs .github/workflows/parse-CDC-metadata.yml

data:
	curl --silent https://data.cdc.gov/data.json > data.json
	curl --silent "https://dashboard.data.gov/validate?schema=federal-v1.1&output=json&datajson_url=https%3A%2F%2Fdata.cdc.gov%2Fdata.json&qa=true" > federal_validation.json
