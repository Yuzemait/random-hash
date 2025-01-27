install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

lint:
	pylint --disable=R,C random_hash.py

test:
	pytest -vv --cov=random_hash --cov-report=term-missing
