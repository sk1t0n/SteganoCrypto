.PHONY: run_tests, run_mypy, run_isort

run_tests:
	python3 -m unittest tests/test_crypto.py

run_mypy:
	python3 -m mypy .

run_isort:
	python3 -m isort .
