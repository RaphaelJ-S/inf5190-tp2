

run: app/src/app.py
	python -m app.src.app

test: testPlanif testService
	python -m unittest discover app/tests

testPlanif: app/tests/planificateur/
	python -m unittest discover app/tests/planificateur
	
testService: app/tests/service/
	python -m unittest discover app/tests/service

doc: app/src/fichier/doc.raml
	raml2html app/src/fichier/doc.raml > app/src/templates/documentation.html

.PHONY: run test testPlanif testService