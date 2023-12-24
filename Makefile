install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

pylint:
	pylint *

test:
	python -m pytest -vv test.py

all: install lint test