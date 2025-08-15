.PHONY: install clean lint type-check format run commit help

help:
	@echo "Available commands:"
	@echo "  make install      - Install dependencies using uv"
	@echo "  make clean        - Clean up Python cache files"
	@echo "  make lint         - Run ruff linter"
	@echo "  make type-check   - Run type checking with mypy"
	@echo "  make format       - Format code with ruff"
	@echo "  make run          - Run the main application"
	@echo "  make commit       - Create a commit using commitizen"
	@echo "  make all         - Run format, lint, and type-check"

install:
	uv pip install -r requirements.txt

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

lint: type-check
	uv run ruff check .

type-check:
	uv run ty check .

format: lint
	ruff format .

run:
	uv run python main.py

commit:
	uv run cz commit

all: format lint type-check
