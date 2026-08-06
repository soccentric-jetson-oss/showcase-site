.PHONY: all serve
all:
	@echo "Static site - no build needed"
serve:
	python3 -m http.server 8080

format:
	@echo "Static site - no formatting needed"

lint:
	@echo "Static site - no linting needed"

doc:
	@echo "Static site - no documentation generation needed"

analyze: format lint doc
