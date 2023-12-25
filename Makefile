install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

pylint:
	pylint *

flake8:
	flake8 *

test:
	python -m unittest

all: install lint test
