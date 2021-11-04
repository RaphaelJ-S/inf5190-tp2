

run: app/src/app.py
	python -m app.src.app

test: 
	python -m unittest discover app/tests

.PHONY: run test