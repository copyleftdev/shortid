.DEFAULT_GOAL := all

version           := $(shell                                        \
			cat setup.py                                \
			| grep '^__version__'                       \
			| sed 's|__version__ = "\([0-9\.]\+\)"|\1|' \
			)

test_requirements := test/requiremets.txt

.PHONY: test-dependencies
test-dependencies: $(test_requirements)
	pip install -r $(test_requirements)

.PHONY: test
test: test-dependencies
	nosetests

.PHONY: tag
tag:
	git tag $(version)

.PHONY: upload
upload: ~/.pypirc
	python setup.py sdist upload -r pypi
