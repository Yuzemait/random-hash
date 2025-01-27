install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

lint:
	pylint --disable=R,C random-hash.py

test:
	pytest -vv --cov=random-hash --cov-report=term-missing
