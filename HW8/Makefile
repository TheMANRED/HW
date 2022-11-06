.PHONY: all \
		setup \
		lint \
		run

venv/bin/activate:
	python3 -m venv venv

setup:
	venv/bin/activate; pip install pip wheel setuptools
	venv/bin/activate; pip install -r requirements.txt
	venv/bin/activate; python3 -m pip install --upgrade pip setuptools wheel

lint:
	venv/bin/activate; black ./
	venv/bin/activate; flake8

run:
	venv/bin/activate
	venv/bin/activate; python main.py