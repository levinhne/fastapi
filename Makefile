.PHONY: activate activate-fish run-dev clean

SHELL := /bin/bash

activate:
	@source venv/bin/activate

activate-fish:
	@source venv/bin/activate.fish

run-dev:
	uvicorn main:app --reload

clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete