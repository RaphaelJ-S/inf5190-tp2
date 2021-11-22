

run: app/src/app.py
	python -m app.src.app

test: testMAJ
	python -m unittest discover app/tests

testMAJ: app/tests/planificateur/test_maj.py
	python -m unittest discover app/tests/planificateur
	
doc: app/src/fichier/doc.raml
	raml2html app/src/fichier/doc.raml > app/src/templates/documentation.html

.PHONY: run test testMAJ