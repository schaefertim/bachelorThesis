.PHONY: help
.PHONY: black black-check flake8
.PHONY: install-lint
.PHONY: black isort format
.PHONY: black-check isort-check format-check
.PHONY: flake8
.PHONY: pydocstyle-check
.PHONY: darglint-check

.DEFAULT: help
help:
	@echo "black"
	@echo "        Run black on the project"
	@echo "black-check"
	@echo "        Check if black would change files"
	@echo "flake8"
	@echo "        Run flake8 on the project"
	@echo "pydocstyle-check"
	@echo "        Run pydocstyle on the project"
	@echo "darglint-check"
	@echo "        Run darglint on the project"
	@echo "isort"
	@echo "        Run isort (sort imports) on the project"
	@echo "isort-check"
	@echo "        Check if isort (sort imports) would change files"
	@echo "install-lint"
	@echo "        Install backpack and linter tools (included in install-dev)"
###
# Linter and autoformatter

# Uses black.toml config instead of pyproject.toml to avoid pip issues. See
# - https://github.com/psf/black/issues/683
# - https://github.com/pypa/pip/pull/6370
# - https://pip.pypa.io/en/stable/reference/pip/#pep-517-and-518-support
black:
	@black . --config=black.toml

black-check:
	@black . --config=black.toml --check

flake8:
	@flake8 .

pydocstyle-check:
	@pydocstyle --count .

darglint-check:
	@darglint --verbosity 2 .

isort:
	@isort . --profile black

isort-check:
	@isort . --check --diff --profile black

format:
	@make black
	@make isort
	@make black-check

format-check: black-check isort-check flake8 pydocstyle-check darglint-check

###
# Installation
install-lint:
	@pip install darglint flake8 mccabe pycodestyle pydocstyle pyflakes pep8-naming flake8-bugbear flake8-comprehensions flake8-tidy-imports black isort
