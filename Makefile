.PHONY: install run test

install:
	python -m pip install -r requirements.txt
	python -m playwright install chromium

run:
	uvicorn app.main:app --host 127.0.0.1 --port 8000

test:
	pytest tests
