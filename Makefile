# Makefile only for development

lint:
	black *.py
	yamllint .github/workflows/parse-CDC-metadata.yml	

edit:
	emacs .github/workflows/parse-CDC-metadata.yml
