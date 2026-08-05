.PHONY: all serve
all:
	@echo "Static site - no build needed"
serve:
	python3 -m http.server 8080
