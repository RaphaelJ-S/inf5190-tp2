

run: app/src/app.py
	python -m app.src.app

test: testPlanif testService testMessagerie
	python -m unittest discover app/tests

testPlanif: app/tests/planificateur/
	python -m unittest discover app/tests/planificateur
	
testService: app/tests/service/
	python -m unittest discover app/tests/service

testMessagerie: app/tests/message/
	python -m unittest discover app/tests/message

doc: app/src/fichier/doc.raml
	raml2html app/src/fichier/doc.raml > app/src/templates/documentation.html

pep8: scripts/pycode.py
	python scripts/pycode.py
	

.PHONY: run test testPlanif testService pep8