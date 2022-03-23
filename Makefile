# Makefile related to requirements
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────

SHELL := bash

MK_FILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
ROOT_PATH := $(realpath $(dir $(MK_FILE_PATH)))

SETUP_PATH = $(ROOT_PATH)/setup
SETUP_CONF_PATH = $(SETUP_PATH)/style_conf

SRC_PATH = $(ROOT_PATH)/src
TESTS_PATH = $(ROOT_PATH)/tests
INI_PATH = $(TESTS_PATH)/pytest.ini

# --------------------------------------------------------------------------------------------------------------------
# --- OPTIONS
# --------------------------------------------------------------------------------------------------------------------

.PHONY: clean-pyc clean-build docs

help: ## This help.
	@echo " Usage: make <task>"
	@echo "   task options:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "	\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

clean: clean-build clean-dist clean-pyc

clean-dist: ## Remove 'dist' folder.
	@rm -fr dist/

clean-build: ## Remove construction artifacts, except 'dist' folder.
	@find $(ROOT_PATH) -name 'build' -exec rm -rf {} +
	@find $(ROOT_PATH) -name '*.egg-info' -exec rm -rf {} +

clean-pyc: ## Remove Python file artifacts.
	@find $(ROOT_PATH) -name '*.pyc' -exec rm -f {} +
	@find $(ROOT_PATH) -name '*.pyo' -exec rm -f {} +
	@find $(ROOT_PATH) -name '*~' -exec rm -f {} +

req-install-dev: ## Install only development requirements in the activated local environment
	@make -f $(SETUP_PATH)/Makefile install-req-dev

req-install: ## Install the required libraries.
	@make -f $(SETUP_PATH)/Makefile install-req

req-remove: ## Uninstall all the libraries installed in the Python environment.
	@make -f $(SETUP_PATH)/Makefile remove-req

req-clean: ## Remove all items from the pip cache.
	@make -f $(SETUP_PATH)/Makefile cache-purge

lint: ## Check style with flake8 and pylint.
	@echo ""
	@echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@echo "─── Checking the project code style [flake8]"
	@echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@flake8 --config=$(SETUP_CONF_PATH)/.flake8 src tests

	@echo ""
	@echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@echo "─── Checking the project code style [pylint]"
	@echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@pylint --rcfile=$(SETUP_CONF_PATH)/.pylintrc src tests

test: ## Run tests quickly with the default Python.
	@cd $(TESTS_PATH) && PYTHONPATH=$(SRC_PATH) pytest -c $(INI_PATH) -rfs $(TESTS_PATH) || true
	@find $(ROOT_PATH) -name '.pytest_cache' -exec rm -rf {} +
	@find $(ROOT_PATH) -name '.coverage*' ! -name ".coveragerc" -exec rm -rf {} +

sdist: clean ## Package as .tar.gz.
	@echo ""
	@echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@echo "─── Setup sdist"
	@echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@python setup.py sdist
	@$(MAKE) clean-build
	@echo ""
	@ls -l dist
	@echo ""

bdist: clean ## Package as .whl (recommended).
	@echo ""
	@echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@echo "─── Setup bdist_wheel"
	@echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────"
	@PYTHONPATH=$(ROOT_PATH) python setup.py clean --all bdist_wheel
	@$(MAKE) clean-build
	@echo ""
	@ls -l dist
	@echo ""