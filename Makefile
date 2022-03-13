lint:
	black *.py
	yamllint .github/workflows/parse-CDC-metadata.yml	

edit_yaml:
	emacs .github/workflows/parse-CDC-metadata.yml
