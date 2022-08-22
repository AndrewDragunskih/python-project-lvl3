install:
	poetry install

test:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml

lint:
	poetry run flake8 page_loader

lint-test:
	poetry run flake8 test

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

page-loader:
	poetry run page-loader

.PHONY: install test lint selfcheck check build
