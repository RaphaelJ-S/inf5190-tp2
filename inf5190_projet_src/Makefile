

run: app/src/app.py
	python -m app.src.app

test: testMAJ
	python -m unittest discover app/tests

testMAJ: app/tests/planificateur/test_maj.py
	python -m unittest discover app/tests/planificateur
	
.PHONY: run test testMAJ