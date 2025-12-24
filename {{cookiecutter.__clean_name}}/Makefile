# .PHONY tells Make that these are commands, not files
.PHONY: help setup format lint type tests tests-all docs serve publish clean

# Default target: Run 'make' or 'make help' to see this menu
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "  setup      Install dependencies (prod + dev) and project in editable mode"
	@echo "  format     Format code using ruff"
	@echo "  lint       Lint code using ruff (with auto-fix)"
	@echo "  type       Typecheck code using ty"
	@echo "  tests      Run ONLY tests affected by recent code changes (testmon)"
	@echo "  tests-all  Run ALL tests"
	@echo "  pr         Run format, lint, type, and INCREMENTAL tests"
	@echo "  docs       Build documentation using mkdocs"
	@echo "  serve      Serve documentation locally"
	@echo "  publish    Publish documentation to GitHub Pages"
	@echo "  clean      Remove cache files (.testmondata, .ruff_cache, etc.)"

setup:
	uv sync

format:
	uv run ruff format ./src

lint:
	uv run ruff check --fix ./src

type:
	uv run ty check ./src

tests:
	uv run pytest --testmon

tests-all:
	uv run pytest --color=yes tests

pr: format lint type tests

docs:
	uv run mkdocs build

serve:
	uv run mkdocs serve

publish:
	uv run mkdocs gh-deploy

# Cleanup is essential for ML projects to clear stale caches
clean:
	rm -rf .pytest_cache .ruff_cache .testmondata site/
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete