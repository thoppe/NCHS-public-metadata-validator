lint:
	black *.py
	yamllint .github/workflows/parse-CDC-metadata.yml	
