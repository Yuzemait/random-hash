install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	pylint --disable=R,C random-hash.py

test:
	python -m pytest -vv --cov=hello random-hash.py