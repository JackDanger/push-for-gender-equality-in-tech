setup:
	which pipenv >/dev/null || pip install pipenv
	pipenv check || pipenv install

develop: setup
	pipenv shell -c

publish: setup
	python convert.py
	cmark output.txt --to html > output.html
	open output.html
